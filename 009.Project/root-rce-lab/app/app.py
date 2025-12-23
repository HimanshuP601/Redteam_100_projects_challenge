from flask import Flask, request
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    ip = request.args.get("ip")
    return os.popen(f"ping -c 1 {ip}").read()

@app.route("/")
def index():
    return "Root RCE Lab Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

