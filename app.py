import os
import socket
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "socket.gethostname()

@app.route('/how are you')
def hello():
    return socket.gethostname()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
