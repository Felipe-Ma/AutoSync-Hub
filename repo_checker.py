# repo_checker.py
from logger_config import *


def check_repositories(webhook_repo, config):
    """Check if the repository is in the list of repositories."""

    print(f"Checking repository: {webhook_repo}")
    # Iterate through each dictionary in the list
    for repo_dict in config.repositories:
        if webhook_repo in repo_dict:
            log_success(f"Repository {webhook_repo} found in the list of repositories.")
            # Return the file path of the repository from the dictionary
            return repo_dict[webhook_repo]
    # If the loop completes without finding the repository, log an error and return None
    log_error(f"Repository {webhook_repo} not found in the list of repositories.")
    return None