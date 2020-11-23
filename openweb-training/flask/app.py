from flask import Flask # Constructor
app = Flask(__name__) # Application

@app.route('/')
def microservices_api():
    return {
        "status": "200 OK",
        "msg":"Welcome to Microservices API in Flask with Python"
    }
if __name__ == '__main__':
    app.run()