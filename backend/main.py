# backend/main.py

from flask import Flask
from uvicorn.middleware.wsgi import WSGIMiddleware

# Your existing Flask app
flask_app = Flask(__name__)

@flask_app.route("/")
def hello_world():
    return "Hello, World!"

# <-- NEW: wrap the Flask WSGI app as ASGI for uvicorn
app = WSGIMiddleware(flask_app)
