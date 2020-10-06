"""
Author: Zach George
Create test cases for the github_repo_info function
"""

import unittest 
from github_information import github_repo_info, HTTPError
from typing import List


class GitHubInformationTest(unittest.TestCase):


    """ Test the github_repo_info function """


    def test_github_repo_info_1(self):

        """ Test a non string input into the function and expect an error """

        with self.assertRaises(ValueError):
            github_repo_info(1)

    def test_github_repo_info_2(self):

        """ Test a fake user_ID into the function and expect an error """

        with self.assertRaises(HTTPError):
            github_repo_info("this_is_a_fake_id")

    def test_github_repo_info_3(self):

        """ Test the richkempinski user_ID and compare to the outputted results """

        self.assertEqual(github_repo_info("richkempinski"), ["Repo: csp Number of commits: 2", 
                                                            "Repo: hellogitworld Number of commits: 30", 
                                                            "Repo: helloworld Number of commits: 6", 
                                                            "Repo: Mocks Number of commits: 10", 
                                                            "Repo: Project1 Number of commits: 2", 
                                                            "Repo: richkempinski.github.io Number of commits: 9", 
                                                            "Repo: threads-of-life Number of commits: 1",
                                                            "Repo: try_nbdev Number of commits: 2", 
                                                            "Repo: try_nbdev2 Number of commits: 5"])


if __name__ == "__main__":
    unittest.main()