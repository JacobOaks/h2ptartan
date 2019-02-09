from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

app.elasticsearch = Elasticsearch([app.config['ELASTICSEARCH_URL']]) \
    if app.config['ELASTICSEARCH_URL'] else None

from app import routes, models, forms, search
