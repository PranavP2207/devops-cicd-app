from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello from the CI/CD Pipeline!</h1><p>This Flask app was built and deployed automatically using GitHub, Jenkins and Docker By Pranav</p>"


@app.route("/health")
def health():
    return jsonify(status="UP")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
