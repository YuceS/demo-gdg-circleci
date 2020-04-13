from flask import Flask
from flask import request
import socket

app = Flask(__name__)

@app.before_request
def log_request():
    app.logger.debug("Request Headers %s", request.headers)
    return None

@app.route("/os")
def os_attr():
    return "Hello " + str(socket.gethostname())

@app.route("/")
def hello():
    return "Web App rocks!! " + ", ".join(request.access_route)


@app.route("/details")
def detay():
    return  ", ".join(request.access_route)

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug='true',port='9999')
