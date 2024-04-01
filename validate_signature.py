import hmac
import hashlib
from logger_config import setup_logger
logger = setup_logger()

# Python file to validate signature
def validate_signature(data, signature, secret_token):
    """ Validate the signature using HMAC SHA-256 algorithm. """
    # Create a new HMAC object using secret token, data, and SHA-256 algorithm
    hmac_gen = hmac.new(secret_token.encode(), data, hashlib.sha256)
    expected_signature = 'sha256=' + hmac_gen.hexdigest() # Generate the expected signature
    """ DEBUGGING """
    print("Expected: " + expected_signature)
    print("Received: " + signature)
    logger.info("Expected: " + expected_signature)
    logger.info("Received: " + signature)
    """ DEBUGGING """
    return hmac.compare_digest(expected_signature, signature) # Compare the expected and received signatures

