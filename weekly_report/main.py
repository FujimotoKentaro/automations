from git import *    #git.~で使用する必要がないようにgit 以下をimport
# url = 'https://gitlab.tokyo.optim.co.jp/optim-store/tools/optim_store_recovery'
# url = 'https://gitlab.tokyo.optim.co.jp/optim-store/tools/bpcc-text-checker'
import datetime
import sys
from enum import Enum


class RepoType(Enum):
    RECOVERY = 1
    CREATE_TEXT = 2


def get_prev_day(prev_days = 0):
    today = datetime.datetime.now(tz = datetime.timezone(datetime.timedelta(hours=9)))
    today.replace(hour=0)
    diff_days = datetime.timedelta(days = prev_days) # 土曜日
    prev_date = today - diff_days

    return prev_date

    # 土　日　月　火　水　木　金　土　日　月
def get_prev_saturday():
    today = get_prev_day()
    if today.weekday() == 0: # Monday
        return get_prev_day(9)
    elif today.weekday() == 6: # Sunday
        return get_prev_day(1)
    else:
        return get_prev_day(today.weekday() + 2)

def get_prev_monday():
    prev_saturday = get_prev_saturday()
    return prev_saturday + datetime.timedelta(days = 2)

def get_prev_friday():
    prev_saturday = get_prev_saturday()
    return prev_saturday + datetime.timedelta(days = 6)


# search_from_commits(made_list, "Fujisan", 144)
def search_from_commits(commit_list, author_name):
    my_commits = []
    prev_saturday = get_prev_saturday()
    for commit in commit_list:
        # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
        # print(commit.committed_datetime.tzname())
        # print(commit.committer_tz_offset)
        # print('----end-----')
        # print(get_oneweek_before(), commit.committed_datetime, get_oneweek_before() <= commit.committed_datetime)
        if commit.author.name == author_name and prev_saturday <= commit.committed_datetime:
            # print (commit.author, commit.message)
            my_commits.append(commit.message)
    return my_commits


def slice_commit(my_commits):
    commit_number_set = set()
    for commit_str in my_commits:
        idx = min(commit_str.find('_') % 10000, commit_str.find(' ') % 10000, commit_str.find('の') % 10000)
        id_number = commit_str[:idx]

        if id_number[:2] == 'No':
            commit_number_set.add(id_number)

    # print(commit_number_list)
    return commit_number_set


def formatter(commit_number_set, repo_type = RepoType.RECOVERY):
    ret_string = ""
    for commit_number in commit_number_set:
        if repo_type == RepoType.RECOVERY:
            text = commit_number + 'のリカバリー'
            ret_string += '・' + text +'\n'
        elif repo_type == RepoType.CREATE_TEXT:
            text = commit_number + 'のテキスト作成'
            ret_string += '・' + text +'\n'
        else:
            ret_string += '登録されていないリポジトリ\n'

    # print(repo_type)
    # print(ret_string)
    print(ret_string, file=sys.stderr)
    return ret_string        

# input: repository url
# output: all commit (restricted commit)
def get_commits_from_path(repo_path):
    #pass #error回避のための何もしない合図

    repo = Repo(repo_path)

    # for item in repo.iter_commits('main',max_count = 10):
    #     print(item.author, item)

    return repo.iter_commits('main')


def execute(git_repo_path, author):
    monday = get_prev_monday().strftime('%m/%d')
    friday = get_prev_friday().strftime('%m/%d')

    output = "{}~{}\n".format(monday,friday)
    for repo_data in git_repo_path:
        path = repo_data["path"]
        repo_type = RepoType.RECOVERY if repo_data["type"] == 'Recovery' else RepoType.CREATE_TEXT

        commit_list = get_commits_from_path(path)
        my_commits = search_from_commits(commit_list, author)
        commit_number_list = slice_commit(my_commits)
        text = formatter(commit_number_list, repo_type)
        output += text

    with open('report.txt','w') as f:
        f.write(output)


if __name__ == '__main__': # おまじない
    import json

    with open('config.json','r') as json_file:
        config_dict = json.load(json_file)
        author = config_dict["author"]
        git_repo_path = config_dict["repository"]
        # print(config_dict)

    execute(git_repo_path, author)
    # datetime
