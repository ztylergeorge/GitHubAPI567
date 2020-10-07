"""
Author: Zach George
Create test cases for the github_repo_info function
UPDATE FOR HW5a:
Create mocks to assist with testing
"""

import unittest 
from unittest.mock import MagicMock as Mock
from unittest.mock import patch 
import github_information
from typing import List
import json


class GitHubInformationTest(unittest.TestCase):


    """ Test the github_information functions using mocks """

    def test_correct_inputs(self):

        """ Check for correct type of inputs """

        with self.assertRaises(TypeError):
            github_information.get_repositories(1)
        with self.assertRaises(TypeError):
            github_information.get_commits_number('foo', 1.2)
        with self.assertRaises(TypeError):
            github_information.get_commits_number(True, 'foo')

    @patch('github_information.get_repositories', return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                              { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]'))

    def test__repositories_names(self, mock1): 

        """ Test the repositories functions and check for names """

        repositories_names: List[str] = list()
        for i in range(6):
            repositories_names.append(github_information.get_repositories('mock1')[i]['name'])
        self.assertIn('Student-Repository', repositories_names)

    @patch('github_information.get_commits_number', return_value = 6)
    def test_commits_numbers(self, mock2):

        """ Test the commits number function by setting value to integer """

        self.assertEqual(github_information.get_commits_number('mock2', 'mock2-repository'), 6)

    @patch('github_information.requests.get')
    def test_error_raising_1(self, mock3):

        """ Test error raising for the repository fetching """

        mock3.return_value.status_code = 404
        with self.assertRaises(github_information.HTTPError):
            github_information.get_repositories('mock3')

    @patch('github_information.requests.get')
    def test_error_raising_2(self, mock4):

        """ Test error raising for the github repo and commit fetching """

        mock4.return_value.status_code = 404
        with self.assertRaises(github_information.HTTPError):
            github_information.github_repo_commit_info('mock4')

    @patch('github_information.requests.get')
    def test_error_raising_3(self, mock5):

        """ Test error raising for the commits fetching """
        
        mock5.return_value.status_code = 404
        with self.assertRaises(github_information.HTTPError):
            github_information.get_commits_number('mock5', 'mock5-repository')

    @patch('github_information.requests.get')
    def test_get_repositories(self, mock6):

        """ Test the get repositories function """

        mock6.return_value.status_code = 200
        mock6.return_value.json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                              { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]')
        expected_values = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                              { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]')

        self.assertEqual(expected_values, github_information.get_repositories("mock6"))

    @patch('github_information.requests.get')
    def test_get_commits_numbers(self, mock7):

        """ Test the get commits numbers function """

        mock7.return_value.status_code = 200
        mock7.return_value.json.return_value = json.loads('[ { " commit " : " hello-world_commit_one " }, \
                                                            { " commit " : " hello-world_commit_two "}, \
                                                            { " commit " : " hello-world_commit_three "} ]')

        self.assertEqual(github_information.get_commits_number("mock7", "mock7-repository"), 3)

    @patch('github_information.create_repos_commit_formatted_list', return_value = ["Repo: GitHub567 Number of commits: 30", 
                                "Repo: hello-world Number of commits: 3", "Repo: hello_world_SSW567 Number of commits: 1", "Repo: SSW_567_Classify_Triangle Number of commits: 2", 
                                "Repo: Student-Repository Number of commits: 19", "Repo: Triangle567 Number of commits: 8"])

    def test_create_repos_commit_formatted_list(self, mock8):

        """ Test the create formatted list of repositories and commits """

        self.assertEqual(github_information.create_repos_commit_formatted_list("mock8"), ["Repo: GitHub567 Number of commits: 30", 
                                "Repo: hello-world Number of commits: 3", "Repo: hello_world_SSW567 Number of commits: 1", 
                                "Repo: SSW_567_Classify_Triangle Number of commits: 2", "Repo: Student-Repository Number of commits: 19",
                                "Repo: Triangle567 Number of commits: 8"])


if __name__ == "__main__":
    unittest.main()