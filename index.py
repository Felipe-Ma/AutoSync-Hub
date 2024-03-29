from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    #return 'Hello, World!'
    return jsonify({"msg": "Hello, World!"})

if __name__ == '__main__':
    # Turn off debug mode in production environment
    app.run(host='0.0.0.0', port=5000, debuf=True)