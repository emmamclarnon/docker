from flask import Flask

app = Flask(__name__)

@app.route('/')
def get_greeting():
    return "Hello from the **Backend Microservice**!"

if __name__ == '__main__':
    # The container will listen on port 5000
    app.run(host='0.0.0.0', port=5000)
