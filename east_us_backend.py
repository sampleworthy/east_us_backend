from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def east_us_backend():
    return jsonify({"message": "This is the East US backend!"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)