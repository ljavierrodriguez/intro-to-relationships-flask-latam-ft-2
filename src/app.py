import os
from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_cors import CORS
from models import db
from routes import api
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db.init_app(app)
Migrate(app, db)
CORS(app)

app.route('/')
def main():
    return jsonify({"message": "REST API FLASK"}), 200

app.register_blueprint(api, url_prefix="/api")

if __name__ == '__main__':
    app.run()