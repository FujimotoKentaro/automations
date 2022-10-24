from git import *    #git.~で使用する必要がないようにgit 以下をimport
# url = 'https://gitlab.tokyo.optim.co.jp/optim-store/tools/optim_store_recovery'
# url = 'https://gitlab.tokyo.optim.co.jp/optim-store/tools/bpcc-text-checker'

from enum import Enum
class RepoType(Enum):
    RECOVERY = 1
    CREATE_TEXT = 2

# search_from_commits(made_list, "Fujisan", 144)
def search_from_commits(commit_list, author_name, project_number):
    my_commits = []
    for commit in commit_list:
        if commit.author.name == author_name:
            # print (commit.author, commit.message)
            my_commits.append(commit.message)
    return my_commits


def slice_commit(my_commits):
    commit_number_list = []
    for commit_str in my_commits:
        target = '_'
        idx = commit_str.find(target)
        id_number = commit_str[:idx]

        if id_number[:2] == 'No':
            commit_number_list.append(id_number)

    print(commit_number_list)
    return commit_number_list


def formatter(commit_number_list, repo_type = RepoType.RECOVERY):
    for a in commit_number_list:
        if repo_type == RepoType.RECOVERY:
            a = a + 'のリカバリー'
            print(a)
        elif repo_type == RepoType.CREATE_TEXT:
            a = a + 'のテキスト作成'
            print(a)
        else:
            print('登録されていないリポジトリ')

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
        my_commits = search_from_commits(commit_list, "Fujimoto Kentaro", 1)
        commit_number_list = slice_commit(my_commits)
        formatter(commit_number_list)
        formatter(commit_number_list, RepoType.CREATE_TEXT)
        formatter(commit_number_list, 123)
        

        