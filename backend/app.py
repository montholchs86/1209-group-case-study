from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Get the DATABASE_URL from the environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://your_user:your_password@your_rds_endpoint:5432/your_db_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
