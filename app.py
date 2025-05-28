import os
import socket
from flask import Flask, request


app = Flask(__name__)

APP_VERSION = "2.0.0"
APP_MESSAGE = "Hello, World!"


@app.route('/')
def hello_world():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    # Список IP-адресов из X-Forwarded-For (если есть)
    forwarded_for = request.headers.getlist("X-Forwarded-For")
    # Последний прокси (или клиент напрямую)
    remote_addr = request.remote_addr

    return {
        "aplication_message": APP_MESSAGE,
        "aplication_version": APP_VERSION,
        "server_hostname": hostname,
        "server_ip_address": ip_address,
        "client_ip_forwarded_for": forwarded_for,
        "client_ip_remote_addr": remote_addr,
        "env": os.environ.get("TEST_ENV", "TEST_ENV not set"),
        "env_secret": os.environ.get("TEST_SECRET_ENV", "TEST_SECRET_ENV not set")
    }


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
