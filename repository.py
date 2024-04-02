import json
from logger_config import *

# Create object for repository
class Repository:
    """ Class to represent a repository. """
    def __init__(self, repo_id=None, repo_name=None, repo_full_name=None, repo_owner=None):
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_full_name = repo_full_name
        self.repo_owner = repo_owner


    @property
    def repo_id(self):
        return self._repo_id

    @repo_id.setter
    def repo_id(self, value):
        self._repo_id = value

    @property
    def repo_name(self):
        return self._repo_name

    @repo_name.setter
    def repo_name(self, value):
        self._repo_name = value

    @property
    def repo_full_name(self):
        return self._repo_full_name

    @repo_full_name.setter
    def repo_full_name(self, value):
        self._repo_full_name = value

    @property
    def repo_owner(self):
        return self._repo_owner

    @repo_owner.setter
    def repo_owner(self, value):
        self._repo_owner = value

def display_info(self):
    print(f"ID: {self._repo_id}")
    print(f"Name: {self._repo_name}")
    print(f"Full Name: {self._repo_full_name}")
    print(f"Owner: {self._repo_owner}")

# Python file to parse repository name
def extract_repository_info(json_data):
    """ Extract repository information from the JSON data. """
    data = json.loads(json_data)

    # Extract the repository information
    repo_id = data['repository']['id']
    repo_name = data['repository']['name']
    repo_full_name = data['repository']['full_name']
    repo_owner = data['repository']['owner']['name']
    repo = Repository(repo_id, repo_name, repo_full_name, repo_owner)

    # Log the repository information
    log_repo_info(repo)
    display_info(repo)

    return repo