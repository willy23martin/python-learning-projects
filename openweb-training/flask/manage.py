from flask_script import Manager
from app_fundamentals.app import app

manager = Manager(app)
app.config["DEBUG"]= True

if __name__ == '__main__':
    manager.run()