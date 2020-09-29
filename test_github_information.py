"""
Author: Zach George
Create test cases for the github_repo_info function
"""

import unittest 
from github_information import github_repo_info, HTTPError


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

        """ Test the richkempinski user_ID and compare to expected keys """

        self.assertEqual(list(github_repo_info("richkempinski").keys()), ['csp', "hellogitworld", "helloworld", "Mocks", 
                                                                    "Project1", "richkempinski.github.io", "threads-of-life",
                                                                    "try_nbdev", "try_nbdev2"])

    def test_github_repo_info_4(self):

        """ Test the richkempinski user_ID and compare to the expected keys and values """

        self.assertEqual(github_repo_info("richkempinski"), {'csp':2, "hellogitworld":30, "helloworld":6, "Mocks":10, 
                                                                "Project1":2, "richkempinski.github.io":9, "threads-of-life":1,
                                                                "try_nbdev":2, "try_nbdev2":5})


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)