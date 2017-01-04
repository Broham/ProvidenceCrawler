import github
import json


def process_repo_contents(repo_contents):
    # for each entry in the repo
    for tree in repo_contents['tree']:
        content_type = tree['type']
        print('content_type --- ', content_type)
        # if type is "blob" get the content
        if content_type == 'blob':
            github.get_file_content(tree)
            print('***blob***')
        elif content_type == 'tree':
            print('***tree***')
            # if type is "tree" get the subtree


if __name__ == '__main__':
    repos, is_next = github.get_repos()
    for repo in repos[0:10]:
        # repoJson = github.getRepo(repo['url'])
        sha = github.get_repo_sha(repo['url'])
        repo_json = github.get_repo_contents(repo['url'], sha)
        process_repo_contents(repo_json)
        # print "content",repoJson

        # print next
        # print repos[1]
