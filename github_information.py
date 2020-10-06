"""
Author: Zach George
Read in a github username
Output the repository names with the number of commits 
"""

import requests 
import json
from typing import Dict, List
from requests import HTTPError as HTTPError

def create_repos_commit_formatted_list(user_ID: str) -> List[str]:

    """ Create formatted list of repositories """

    #create list of items 
    outputted_list: List[str] = list()

    #get dictionary of repositories and commits 
    repositories_commits_dictionary = github_repo_commit_info(user_ID)

    #add to list 
    for item in repositories_commits_dictionary.keys():
        outputted_list.append(f"Repo: {item} Number of commits: {repositories_commits_dictionary[item]}")

    #output results 
    return outputted_list

def github_repo_commit_info(user_ID: str) -> Dict[str, int]:

    """ Read in github username and output the repositories with number of commits """
    
    #create repository dictionary
    repos_commit_dict: Dict[str: int] = dict() #key: repos value: commit

    #get the repositories
    repositories = get_repositories(user_ID)

    #add repository name with number of commits 
    for repository in repositories:
        repo = repository['name']
        repos_commit_dict[repo] = get_commits_number(user_ID, repo)

    #return dictionary 
    return repos_commit_dict

def get_repositories(user_ID: str) -> List[str]:

    """ Get the repositories from a user_ID """

    #determine if the user_ID is a string
    if not isinstance(user_ID, str):
        raise ValueError(f"{user_ID} is not a string.")

    #get url for repository
    user_repos = "https://api.github.com/users/" + user_ID + "/repos"

    #attempt to contact website 
    repos_response = requests.get(user_repos)
    if repos_response.status_code != 200:
        raise HTTPError(f"{user_repos} could not be reached.")
    else:
        repos_json_info = repos_response.json()

    #return information 
    return repos_json_info

def get_commits_number(user_ID: str, repo_name: str) -> int:

    """ Get the number of commits for a repository """
    
    #reach the commits from the user_ID and repository name
    commits = "https://api.github.com/repos/" + user_ID + "/" + repo_name + "/commits"
    commits_response = requests.get(commits)

    if commits_response != 200:
        raise HTTPError(f"{commits} could not be reached.")
    else:
        #get json data
        commits_json_info = commits_response.json()

    #return length (number of commits)
    return len(commits_json_info)

#print(create_repos_commit_formatted_list("richkempinski"))