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

    # print(commit_number_list)
    return commit_number_list


def formatter(commit_number_list, repo_type = RepoType.RECOVERY):
    ret_string = ""
    for commit_number in commit_number_list:
        if repo_type == RepoType.RECOVERY:
            text = commit_number + 'のリカバリー'
            ret_string += text +'\n'
        elif repo_type == RepoType.CREATE_TEXT:
            text = commit_number + 'のテキスト作成'
            ret_string += text +'\n'
        else:
            ret_string += '登録されていないリポジトリ\n'

    # print(repo_type)
    # print(ret_string)
    return ret_string        

# input: repository url
# output: all commit (restricted commit)
def get_commits_from_path(repo_path):
    #pass #error回避のための何もしない合図

    repo = Repo(repo_path)

    # for item in repo.iter_commits('main',max_count = 10):
    #     print(item.author, item)

    return repo.iter_commits('main')


def execute(git_repo_path):
    for repo_data in git_repo_path:
        path = repo_data[0]
        repo_type = repo_data[1]
        commit_list = get_commits_from_path(path)
        my_commits = search_from_commits(commit_list, "Fujimoto Kentaro", 1)
        commit_number_list = slice_commit(my_commits)
        text = formatter(commit_number_list, repo_type)

        with open('write_test.txt','w') as f:
            f.write(text)


if __name__ == '__main__': # おまじない
    git_repo_paths = [('..', RepoType.RECOVERY)]
    execute(git_repo_paths)
    
