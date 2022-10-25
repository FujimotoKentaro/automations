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
