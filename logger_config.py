# logger_config.py
import logging


# Create a logger
logger = logging.getLogger('webhook_logger')
logger.setLevel(logging.DEBUG)

# Create a file handler
handler = logging.FileHandler('webhook.log')
handler.setLevel(logging.DEBUG)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(handler)



def log_repo_info(repo):
    # Log repository information in a single line
    logger.info(f"Repository: {repo._repo_name} - {repo._repo_full_name} - {repo._repo_owner}")

def log_key(key, value):
    # Log the key and value in a single line
    logger.info(f"{key}: {value}")

def log_config(config):
    # Log the configuration in a single line
    logger.info(f"Configuration loaded: {config._repositories} - {config._port} - {config._secret_token}")

def log_error(error):
    # Log the error message
    logger.error(error)

def log_success(message):
    # Log the success message
    logger.info(message)

def log_signature_validation(expected, received):
    # Log the expected and received signatures
    logger.info(f"Expected: {expected}")
    logger.info(f"Received: {received}")