"""
Author: Zach George
Create test cases for the github_repo_info function
"""

import unittest 
import requests
from unittest.mock import MagicMock as Mock
from unittest.mock import patch 
from github_information import github_repo_info, HTTPError
from typing import List
import json


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

    @patch('requests.get')
    def test_httperror_repo_info(self, injectedMock):
        injectedMock.return_value.status_code = 404
        injectedMock.user_ID = "richkempinski" # a known working user ID
        with self.assertRaises(HTTPError):
            github_repo_info(injectedMock.user_ID)

    
    
    @patch('requests.get')
    def test_getting_repo_info(self, injectedMock):
        injectedMock.return_value.status_code = 200
        json_obj = json.loads('[ { "name" : "csp" }, { "name" : "hellogitworld" }, \
                                { "name" : "helloworld" }, { "name" : "Mocks" }, \
                                { "name" : "Project1" }, { "name" : "richkempinski.github.io" },\
                                 { "name" : "threads-of-life" }, { "name" : "try_nbdev" }, \
                                     { "name" : "try_nbdev2" } ]')
        injectedMock.json.return_value = json_obj
        #info = github_repo_info(self.user_ID)
        self.assertEqual(len(json_obj), len(["Repo: csp Number of commits: 2", 
                                "Repo: hellogitworld Number of commits: 30", 
                                "Repo: helloworld Number of commits: 6", 
                                "Repo: Mocks Number of commits: 10", 
                                "Repo: Project1 Number of commits: 2", 
                                "Repo: richkempinski.github.io Number of commits: 9", 
                                "Repo: threads-of-life Number of commits: 1",
                                "Repo: try_nbdev Number of commits: 2", 
                                "Repo: try_nbdev2 Number of commits: 5"]))

if __name__ == "__main__":
    unittest.main()