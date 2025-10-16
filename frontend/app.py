from flask import Flask
import requests
import os

app = Flask(__name__)

# The hostname 'backend' is resolved by Docker Compose's internal network DNS
# The port is 5000, as defined in the backend app.py
BACKEND_URL = os.environ.get('BACKEND_URL', 'http://backend:5000')

@app.route('/')
def home():
    try:
        # Call the backend service
        response = requests.get(BACKEND_URL)
        greeting = response.text
    except requests.exceptions.ConnectionError:
        greeting = "Error: Could not connect to backend service."

    return f"""
        <h1>Frontend App Running</h1>
        <p>Received Greeting: <strong>{greeting}</strong></p>
        <p style="background-color:Tomato;">This shows the frontend and backend are communicating!</p>
    """

if __name__ == '__main__':
    # The container will listen on port 8000
    app.run(host='0.0.0.0', port=8000)
