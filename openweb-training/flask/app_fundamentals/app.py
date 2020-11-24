from flask import Flask # Constructor
app = Flask(__name__) # Application

contacts = [
            {
                "contact": {
                    "id": 1123231,
                    "name": "Name A"
                }
            },
            {
                "contact": {
                    "id": 1125261,
                    "name": "Name B"
                }
            }
        ]

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
        "contacts": contacts
    }

@app.route('/contacts/<int:id>')
def contacts_api_contact_endpoint(id):
    response = {
        "status": '404 Not Found',
        "msg": f"There is no contact with id: {id} in our database"
    }
    for index in range(0, len(contacts)):
        if contacts[index]["contact"]["id"] == id:
            response = {
                "status": "200 OK",
                "msg": contacts[index]
            }
            break
    return response

# Remove if you use manager.py
if __name__ == '__main__':
    app.run('0.0.0.0', 5000, debug=True) # Run web server, accept requests from any source by the port 5000 and run it in debug mode
