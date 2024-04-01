# config_loader.py
import yaml
import logging
from logger_config import *

# Class for configuration loader
class ConfigLoader:
    """Class to load configuration from a YAML file. """
    def __init__(self, repositories=None, port=None, secret_token=None):
        self.repositories = repositories
        self.port = port
        self.secret_token = secret_token

    @property
    def repositories(self):
        return self._repositories

    @repositories.setter
    def repositories(self, value):
        self._repositories = value

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, value):
        self._port = value

    @property
    def secret_token(self):
        return self._secret_token

    @secret_token.setter
    def secret_token(self, value):
        self._secret_token = value

def display_info(self):
    print(f"Repositories: {self._repositories}")
    print(f"Port: {self._port}")
    print(f"Secret Token: {self._secret_token}")

def load_config_key(config, key):
    try:
        value = config[key]
        log_success(f"Loaded {key}: {value}")
        return value
    except KeyError:
        print(f"No {key} found in the configuration.")
        return None

def load_config():
    with open('config.yaml', 'r') as file:
        try:
            config = yaml.safe_load(file)
            repositories = load_config_key(config, 'REPOSITORIES')
            port = load_config_key(config, 'PORT')
            secret_token = load_config_key(config, 'SECRET_TOKEN')
            config_loaded = ConfigLoader(repositories, port, secret_token)

            log_config(config_loaded)
            return config_loaded

        except yaml.YAMLError as exc:
            log_error(f"Error loading configuration: {exc}")
            return None

