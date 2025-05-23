import os
import socket
from flask import Flask


app = Flask(__name__)

APP_VERSION = "1.0.0"
APP_MESSAGE = "Hello, World!"


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return {
        "aplication_message": APP_MESSAGE,
        "aplication_version": APP_VERSION,
        "server_hostname": hostname,
        "server_ip_address": ip_address,
        "env": os.environ.get("TEST_ENV", "TEST_ENV not set"),
        "env_secret": os.environ.get("TEST_SECRET_ENV", "TEST_SECRET_ENV not set")
    }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
