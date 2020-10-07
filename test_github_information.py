"""
Author: Zach George
Create test cases for the github_repo_info function
"""

import unittest 
from unittest.mock import MagicMock as Mock
from unittest.mock import patch 
import github_information
from typing import List
import json


class GitHubInformationTest(unittest.TestCase):


    """ Test the github_repo_info function using mocks """

    @patch('github_information.get_repositories', return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                              { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]'))

    @patch('github_information.get_commits_number', return_value = 6)

    def test_commits_counts(self, mock1, mock2): #mock1 is for calling the repository, mock2 is for calling the commits 

        """ Test the commits counts function using mocks """

        self.assertEqual(github_information.get_commits_number('Mock'), 6)
        repositories_names: List[str] = list()
        for i in range(6):
            repositories_names.append(github_information.get_repositories('Mock')[i]['name'])
        self.assertIn('Student-Repository', repositories_names)

    @patch('github_information.requests.get')
    def test_error_raising_1(self, mock3):

        """ Test error raising for the repository fetching """

        mock3.return_value.status_code = 404
        with self.assertRaises(github_information.HTTPError):
            github_information.get_repositories('Mock')

    @patch('github_information.requests.get')
    def test_error_raising_2(self, mock4):

        """ Test error raising for the github repo and commit fetching """

        mock4.return_value.status_code = 404
        with self.assertRaises(github_information.HTTPError):
            github_information.github_repo_commit_info('Mock')

    @patch('github_information.requests.get')
    def test_error_raising_3(self, mock5):

        """ Test error raising for the commits fetching """
        
        mock5.return_value.status_code = 404
        with self.assertRaises(github_information.HTTPError):
            github_information.get_commits_number('Mock', 'Mock-Repository')

    @patch('github_information.requests.get')
    def test_get_repositories(self, mock6):

        """ Test the get repositories function """

        mock6.return_value.json.return_value = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                              { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]')

        print(github_information.get_repositories("Mock"))

        expected_values = json.loads('[ { "name" : "GitHubAPI567" }, { "name" : "hello-world" }, \
                              { "name" : "hello_world_SSW567" }, { "name" : "SSW567_Classify_Triangle" }, \
                                { "name" : "Student-Repository" }, { "name" : "Triangle567" } ]')

        self.assertEqual(expected_values, github_information.get_repositories("Mock"))

    @patch('github_information.requests.get')
    def test_get_commits_numbers(self, mock7):

        """ Test the get commits numbers function """

        mock7.return_value.json.return_value = json.loads('[ { " commits ": " test "}]')
        commits = github_information.get_commits_number("Mock", "Mock-Repos")
        self.assertEqual(commits, 1)



if __name__ == "__main__":
    unittest.main(verbosity = 2, exit=False)