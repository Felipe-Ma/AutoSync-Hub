from flask import Flask, request, abort
import subprocess
import hmac
import hashlib
import json
from datetime import datetime

app = Flask(__name__)

# Your secret token; keep this safe!
SECRET_TOKEN = 'd6b7102b2fd1d510fd9fa44343e2a24c2b6a303e01288b47689acab522dd5a5d'

def validate_signature(data, signature):
    """
    Validate the signature using HMAC SHA-256 algorithm.
    """
    hmac_gen = hmac.new(SECRET_TOKEN.encode(), data, hashlib.sha256)
    expected_signature = 'sha256=' + hmac_gen.hexdigest()
    return hmac.compare_digest(expected_signature, signature)

def git_pull(directory):
    """
    Execute 'git pull' command in the given directory.
    """
    # Change to the specified directory
    subprocess.run(["git", "-C", directory, "pull", "origin", "main"], check=True)

def log_payload(payload):
    """
    Log the webhook payload to a file.
    """
    with open('/root/Desktop/webhook_payloads.log', 'a') as file:  # Specify the path to your log file
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        file.write(f"Timestamp: {timestamp}\n")
        file.write(json.dumps(payload, indent=4))
        file.write("\n\n---\n\n")  # Delimiter for readability

@app.route('/webhook', methods=['POST'])
def webhook():
    # Retrieve the GitHub signature from the headers
    signature = request.headers.get('X-Hub-Signature-256')
    if signature is None:
        abort(400, 'GitHub signature missing.')

    # Verify the signature
    if not validate_signature(request.data, signature):
        abort(401, 'Invalid signature.')

    # Parse the JSON payload
    payload = request.json

    # Log the payload
    log_payload(payload)

    # Define the path to the directory containing your repository
    git_dir = "/root/Desktop/timer-app"

    # Execute git pull
    git_pull(git_dir)

    return 'Success', 200

if __name__ == '__main__':
    app.run(port=80)
