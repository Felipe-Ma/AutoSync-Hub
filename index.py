# index.py
from flask import Flask, jsonify, request
from validate_signature import *
from repository import *
from config_loader import *
from repo_checker import *

app = Flask(__name__)

# Global variables
REPOSITORIES = {}
PORT = 0
SECRET_TOKEN = ''

@app.route('/')
def hello_world():
    return 'Hello, World!'
    #return jsonify({"msg": "Hello, World!"})

@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({"msg": "Hello, World!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    config = app.config['my_config']

    # Secret Token Validation
    signature = request.headers.get('X-Hub-Signature-256')
    if signature is None:
        log_error("GitHub signature missing.")
        return jsonify({"msg": "GitHub signature missing."}), 400

    # Verify the signature
    if not validate_signature(request.data, signature, SECRET_TOKEN):
        log_error("Invalid signature.")
        return jsonify({"msg": "Invalid signature."}), 401

    # Data Extraction
    data = request.data

    # Extract the repository information
    repo = extract_repository_info(data)

    # Check if the repository is in the list of repositories
    if check_repositories(repo._repo_name, config):
        log_success(f"Repository {repo._repo_name} found in the list of repositories.")
        return jsonify({"msg": "Repository found in the list of repositories."})
    else:
        log_error(f"Repository {repo._repo_name} not found in the list of repositories.")
        return jsonify({"msg": "Repository not found in the list of repositories."})

    return jsonify({"msg": "Webhook received"})

#

if __name__ == '__main__':
    # Load the configuration
    config = load_config()
    app.config['my_config'] = config # Store the configuration in the app

    REPOSITORIES, PORT, SECRET_TOKEN = config.repositories, config.port, config.secret_token

    # Turn off debug mode in production environment
    app.run(host='0.0.0.0', port=5000, debug=True)