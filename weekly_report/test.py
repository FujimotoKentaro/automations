import unittest
import main
from git import *

class TestMain(unittest.TestCase):
    def test_get_commits_from_path(self):
        commits_iter = main.get_commits_from_path("..")
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
