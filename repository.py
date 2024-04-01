import json
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

# Python file to parse repository name
def parse_repository_name():
    """ Parse the repository name from the data. """
    repository_name = data['repository']['name'] # Extract the repository name from the data
