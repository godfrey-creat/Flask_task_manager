from flask import Flask
from config import Config
from models import db, bcrypt
from routes import app

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
bcrypt.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

