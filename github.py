import requests
import re
import base64
import os
import config

with requests.Session() as session:

    session.auth = (config.user, config.password)
    def get_repos(since=0):
        '''
        Place Holder Comment
        '''
        url = 'http://api.github.com/repositories'

        data = """{
          since: %s
        }""" % since
        # request = Request(url)
        # request.add_header('Authorization', 'token %s' % 'e8265f5a3367135bd923154ab64556c49b1500c9')

        response = session.get(url, data=data)
        if response.status_code == 403:
            print('Problem making request!', response.status_code)
            print(response.headers)
        matches = re.match(r'<.+?>', response.headers['Link'])
        is_next = matches.group(0)[1:-1]
        return response.json(), is_next


    def get_repo(url):
        '''
        Place Holder Comment
        '''
        response = session.get(url)
        return response.json()


    def get_read_me(url):
        '''
        Place Holder Comment
        '''
        # Grabs the readme file associated with the current repository
        url += '/readme'
        response = session.get(url)
        return response.json()


    # todo: return array of all commits so we can examine each one 
    def get_repo_sha(url):
        '''
        Place Holder Comment
        '''
        # /repos/:owner/:repo/commits
        commits = session.get(url + '/commits').json()
        return commits[0]['sha']


    def get_all_repo_sha(url):
        '''
        Place Holder Comment
        '''
        commits = session.get(url + '/commits').json()
        all_sha = []
        for x in range(len(commits)):
            all_sha[x] = commits[x]['sha']
        return all_sha


    def get_file_content(item):
        '''
        Place Holder Comment
        '''
        ignore_extensions = ['jpg']
        filename, extension = os.path.splitext(item['path'])
        if extension in ignore_extensions:
            return []
        content = session.get(item['url']).json()
        lines = content['content'].split('\n')
        lines = map(base64.b64decode, lines)
        print('path', item['path'])
        print('lines', "".join(lines[:5]))
        return "".join(lines)


    def get_repo_contents(url, sha):
        '''
        Place Holder Comment
        '''
        # /repos/:owner/:repo/git/trees/:sha?recursive=1
        url += '/git/trees/%s?recursive=1' % sha
        # print 'url', url
        response = session.get(url)
        return response.json()
