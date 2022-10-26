import unittest
import main
from git import *

class TestMain(unittest.TestCase):
    def test_get_commits_from_path(self):
        commits_iter = main.get_commits_from_path("..")
        self.assertTrue(False)

    def test_slice_commit(self):
        name = main.slice_commit(["No123_commit"])
        self.assertTrue(['No123'] == name)

if __name__ == '__main__':
    unittest.main()


# 月曜日の日にち~金曜日の日にち
# ・No177クエリ修正
# ・No178クエリ修正
# ・No167リカバリー
# ・No197リカバリー
# ・No110プレ適応、テキスト比較
# ・お詫びメールの作成（金額修正、二重購入、解約通知忘れ）
# ・No203リカバリー