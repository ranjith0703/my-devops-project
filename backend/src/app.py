from flask import Flask, jsonify
from flask_cors import CORS
from web3 import Web3

app = Flask(__name__)
CORS(app)

w3 = Web3(Web3.HTTPProvider("http://blockchain:8545"))

@app.route("/")
def home():
    return jsonify("Backend is running successfully!")

@app.route("/blockchain")
def blockchain():
    if w3.is_connected():
        return jsonify({
            "message": "Hello Blockchain",
            "block_number": w3.eth.block_number
        })
    else:
        return jsonify({"error": "Blockchain not connected"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)