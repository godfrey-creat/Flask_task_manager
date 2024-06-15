from flask import Flask
from config import Config
from models import db, bcrypt
from routes import app
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config.from_object(Config)
db.init_app(app)
bcrypt.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

