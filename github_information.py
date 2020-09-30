"""
Author: Zach George
Read in a github username
Output the repository names with the number of commits 
"""

import requests 
import json
from typing import Dict, List
from requests import HTTPError as HTTPError

def github_repo_info(user_ID: str) -> Dict[str, int]:

    """ Read in github username and output the repositories with number of commits """

    #determine if the user_ID is a string
    if not isinstance(user_ID, str):
        raise ValueError(f"{user_ID} is not a string.")

    #create repository dictionary and user repository string
    repos_dict: Dict[str: int] = dict() #key: repos value: commit
    user_repos = "https://api.github.com/users/" + user_ID + "/repos"
    
    #attempt to contact website 
    repos_response = requests.get(user_repos)
    if repos_response.status_code != 200:
        raise HTTPError(f"{user_repos} could not be reached.")
    else:
        repos_json_info = repos_response.json()

        #take in the name of the repository
        for i in range(0, len(repos_json_info)):
            repos_dict[repos_json_info[i]["name"]] = 0

        #determine number of commits per repository
        for repos in repos_dict.keys():
            commits = "https://api.github.com/repos/" + user_ID + "/" + repos + "/commits"
            commits_response = requests.get(commits)
            commits_json_info = commits_response.json()
            repos_dict[repos] = len(commits_json_info)

    #create list of items 
    outputted_list: List[str] = list()
    for repos in repos_dict.keys():
        outputted_list.append(f"Repo: {repos} Number of commits: {repos_dict[repos]}")

    #output results 
    return outputted_list