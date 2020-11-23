from flask import Flask # Constructor
app = Flask(__name__) # Application

@app.route('/') # Decortator - main route of the application
def microservices_api(): # Without parameters
    return {
        "status": "200 OK",
        "msg":"Welcome to Microservices API in Flask with Python"
    } # HTTP response object
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True) # Run web server, accept requests from any source by the port 5000 and run it in debug mode