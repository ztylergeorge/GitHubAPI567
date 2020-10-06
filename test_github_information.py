"""
Author: Zach George
Create test cases for the github_repo_info function
"""

import unittest 
from unittest.mock import MagicMock as Mock
from unittest.mock import patch 
from github_information
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

    @patch('github_information.requests.get')
    def test_httperror_repo_info(self, injectedMock):

        """ Test using Mock and fake user ID """

        injectedMock.return_value = 404
        user_ID = "this_is_a_fake_ID" # a known fake user ID
        with self.assertRaises(HTTPError):
            github_repo_info(Mock)

    @patch('github_information.requests.get')
    def test_getting_repo_info(self, injectedMock):

        """ Test using Mock and real user ID """

        injectedMock.return_value = ["Repo: GitHub567 Number of commits: 30", 
                                "Repo: hello-world Number of commits: 3", 
                                "Repo: hello_world_SSW567 Number of commits: 1", 
                                "Repo: SSW_567_Classify_Triangle Number of commits: 2", 
                                "Repo: Student-Repository Number of commits: 19", 
                                "Repo: Triangle567 Number of commits: 8"]

      #  json_obj = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
       #                         { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
       #                         { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]')      
        results: List[Mock] = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        results[0].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
        results[1].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
        results[2].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
        results[3].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
        results[4].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
        results[5].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
        results[6].json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                                { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]') 
  
        injectedMock.side_effect = results
        #injectedMock.user_ID = "ztylergeorge"
        #info = github_repo_info(self.user_ID)
        actual = Mock
        #print(github_repo_info("ztylergeorge"))
        self.assertEqual(github_repo_info(actual), ["Repo: GitHub567 Number of commits: 30", 
                                "Repo: hello-world Number of commits: 3", 
                                "Repo: hello_world_SSW567 Number of commits: 1", 
                                "Repo: SSW_567_Classify_Triangle Number of commits: 2", 
                                "Repo: Student-Repository Number of commits: 19", 
                                "Repo: Triangle567 Number of commits: 8"])

if __name__ == "__main__":
    unittest.main(verbosity = 2, exit=False)