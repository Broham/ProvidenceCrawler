import requests
import re
import base64
import os

def getRepos(since=0):
  url = 'http://api.github.com/repositories'
  data = """{
    since: %s
  }""" % since
  response = requests.get(url, data=data)
  if response.status_code == 403:
    print "Problem making request!", response.status_code
    print response.headers
  matches = re.match(r'<.+?>', response.headers['Link'])
  next = matches.group(0)[1:-1]
  return response.json(), next

def getRepo(url):
  response = requests.get(url)
  return response.json()

def getReadMe(url):
  url = url + "/readme"
  response = requests.get(url)
  return response.json()

# todo: return array of all commits so we can examine each one 
def getRepoSHA(url):
  # /repos/:owner/:repo/commits
  commits = requests.get(url + "/commits").json()
  return commits[0]['sha']

def getFileContent(item):
  ignoreExtensions = ['jpg']
  filename, extension = os.path.splitext(item['path'])
  if extension in ignoreExtensions:
    return []
  content = requests.get(item['url']).json()
  lines = content['content'].split('\n')
  lines = map(base64.b64decode, lines)
  print 'path', item['path']
  print 'lines', "".join(lines[:5])
  return "".join(lines)

def getRepoContents(url, sha):
  # /repos/:owner/:repo/git/trees/:sha?recursive=1
  url = url + ('/git/trees/%s?recursive=1' % sha)
  # print 'url', url
  response = requests.get(url)
  return response.json()