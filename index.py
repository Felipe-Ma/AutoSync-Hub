# index.py
from flask import Flask, jsonify, request
from validate_signature import *
from repository import *
from config_loader import *

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
    # Secret Token Validation
    signature = request.headers.get('X-Hub-Signature-256')
    if signature is None:
        #webhook_logger.error("GitHub signature missing.")
        return jsonify({"msg": "GitHub signature missing."}), 400
    # Verify the signature
    if not validate_signature(request.data, signature, SECRET_TOKEN):
        #webhook_logger.error("Invalid signature.")
        print(signature)
       # return expected signature and received signature

        #return jsonify({"expected_signature": SECRET_TOKEN, "received_signature": signature}), 400
        return jsonify({"msg": "Invalid signature."}), 401

    # Parse the repository name
    data = request.data

    repo = extract_repository_info(data)
    return jsonify({"msg": "Webhook received"})

# Identify the repository the webhook is associated with
#def get_repository(data):




if __name__ == '__main__':
    #REPOSITORIES, PORT, SECRET_TOKEN = load_config()
    #print(REPOSITORIES)
    #print(PORT)
    #print(SECRET_TOKEN)
    # Load the configuration
    config = load_config()
    REPOSITORIES = config.repositories
    PORT = config.port
    SECRET_TOKEN = config.secret_token


    # Turn off debug mode in production environment
    app.run(host='0.0.0.0', port=5000, debug=True)