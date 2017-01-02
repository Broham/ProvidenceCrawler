import github
import json

def processRepoContents(repoContents):
  # for each entry in the repo
  for tree in repoContents['tree']:
    contentType = tree['type']
    print 'contentType --- ', contentType
    # if type is "blob" get the content
    if contentType == 'blob':
      github.getFileContent(tree)
      print '***blob***'
    elif contentType == 'tree':
      print '***tree***'
      # if type is "tree" get the subtree

if __name__ == '__main__':
  repos, next = github.getRepos()
  for repo in repos[0:10]:
    # repoJson = github.getRepo(repo['url'])
    sha = github.getRepoSHA(repo['url'])
    repoJson = github.getRepoContents(repo['url'], sha)
    processRepoContents(repoJson)
    # print "content",repoJson

  # print next
  # print repos[1]


