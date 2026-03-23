from flask_sqlalchemy import SQLAlchemy
import redis
from flask_migrate import Migrate 

db = SQLAlchemy()
migrate = Migrate()
redis_client = redis.Redis.from_url("redis://redis:6379/0")
