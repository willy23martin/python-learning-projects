from flask import Flask # Constructor
app = Flask(__name__) # Application

@app.route('/') # Decortator - main route of the application
def microservices_api(): # Without parameters
    # Only for debugging purposes
    # a = 'Basic Flask web application'
    # b = int(a) # For debugging using the PIN

    # HTTP response JSON Object
    return {
        "status": "200 OK",
        "msg":"Welcome to Microservices API in Flask with Python"
    }


@app.route('/contacts/') # Between /.../ in order to grant the navigation to this endpoint
def contacts_api():
    return {
        "contacts": [
            {
                "contact": 1123231
            },
            {
                "contact": 1125262
            }
        ]
    }

# Remove if you use manager.py
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True) # Run web server, accept requests from any source by the port 5000 and run it in debug mode
