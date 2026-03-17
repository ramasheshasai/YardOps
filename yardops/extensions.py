from flask_sqlalchemy import SQLAlchemy
from redis import Redis
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()
redis_client = None
