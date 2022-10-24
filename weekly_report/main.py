from git import *    #git.~で使用する必要がないようにgit 以下をimport
# url = 'https://gitlab.tokyo.optim.co.jp/optim-store/tools/optim_store_recovery'
# url = 'https://gitlab.tokyo.optim.co.jp/optim-store/tools/bpcc-text-checker'

# search_from_commits(made_list, "Fujisan", 144)
def search_from_commits(commit_list, author_name, project_number):
    list = []
    for commit in commit_list:
        if commit.author.name == author_name:
            # print (commit.author, commit.message)
            list.append(commit.message)
    return list

def slice_commit(list):
    for commit in list :
        s = commit
        target = '_'
        idx = s.find(target)
        r = s[:idx]
        print(r)

# input: repository url
# output: all commit (restricted commit)
def get_commits_from_path(repo_path):
    #pass #error回避のための何もしない合図

    repo = Repo(repo_path)

    # for item in repo.iter_commits('main',max_count = 10):
    #     print(item.author, item)

    return repo.iter_commits('main')


if __name__ == '__main__': # おまじない
    git_repo_paths = ['..']
    for path in git_repo_paths:
        commit_list = get_commits_from_path(path)
        list = search_from_commits(commit_list, "FujimotoKentaro", 1)
        slice_commit(list)
        