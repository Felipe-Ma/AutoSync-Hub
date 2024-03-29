import os.path

from flask import Flask, jsonify, request
import yaml
import logging

app = Flask(__name__)

# Global variables
REPOSITORIES = {}
PORT = 0
SECRET_TOKEN = ''

# Set up logging for the /webhook route
log_path = os.path.dirname(os.path.realpath(__file__))
webhook_log = os.path.join(log_path, 'webhook.log')

# Create a specific logger for the webhook
webhook_logger = logging.getLogger('webhook_logger')
webhook_logger.setLevel(logging.INFO)

# Create file handler which logs even debug messages
fh = logging.FileHandler(webhook_log)
fh.setLevel(logging.INFO)

# Create formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setFormatter(formatter)

# Add the handler to the logger
webhook_logger.addHandler(fh)


@app.route('/')
def hello_world():
    return 'Hello, World!'
    #return jsonify({"msg": "Hello, World!"})

@app.route('/hello', methods=['GET'])
def say_hello():
    return jsonify({"msg": "Hello, World!"})

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    #print(data)
    webhook_logger.info("Webhook received")
    return jsonify({"msg": "Webhook received"})

def load_config():
    global REPOSITORIES # Reference the global hash table
    global PORT # Reference the global port variable
    global SECRET_TOKEN # Reference the global secret token

    # Open YAML file and load the configuration
    with open('config.yaml', 'r') as file:
        try:
            config = yaml.safe_load(file)
            # Load the repositories from the configuration
            try:
                REPOSITORIES = config['REPOSITORIES']
                logging.info(f"Repositories loaded: {REPOSITORIES}")
                # Check if the repositories are empty
                if not REPOSITORIES:
                    logging.error("No repositories found in the configuration.")
                    print("No repositories found in the configuration.")
            except KeyError:
                logging.error("No repositories found in the configuration.")

            # Load the port from the configuration
            try:
                PORT = config['PORT']
                logging.info(f"Port loaded: {PORT}")
                # Check if the port is empty
                if not PORT:
                    logging.error("No port found in the configuration.")
                    print("No port found in the configuration.")
            except KeyError:
                logging.error("No port found in the configuration.")

            # Load the secret token from the configuration
            try:
                SECRET_TOKEN = config['SECRET_TOKEN']
                logging.info(f"Secret token loaded: {SECRET_TOKEN}")
                # Check if the secret token is empty
                if not SECRET_TOKEN:
                    logging.error("No secret token found in the configuration.")
                    print("No secret token found in the configuration.")
            except KeyError:
                logging.error("No secret token found in the configuration.")


            logging.info(f"Configuration loaded: {config}")
        except yaml.YAMLError as exc:
            # log to file in the same directory
            logging.error(f"Error loading configuration: {exc}")
        return config




if __name__ == '__main__':
    load_config()
    print(REPOSITORIES)
    print(PORT)
    print(SECRET_TOKEN)

    # Turn off debug mode in production environment
    #app.run(host='0.0.0.0', port=5000, debug=True)