import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL") 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = os.getenv("REDIS_URL")

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:postgres@postgres:5432/yardops_test"