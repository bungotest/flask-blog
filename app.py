from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import pytz
import os

# create the app
app = Flask(__name__)

# Get the directory of the current script
database_file=os.path.abspath(os.path.dirname(__file__))

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(database_file, 'blog.db')}"
db = SQLAlchemy(app)

# Now you can create the database↓DB作成時の使用
# if __name__ == "__main__":
#     with app.app_context():
#         db.create_all()
#     print("Database created successfully!")

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    body = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now(pytz.timezone('America/Los_Angeles')))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user/<name>")
def user(name):
    return f"This is {name}'s page!"

