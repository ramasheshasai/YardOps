import pytest
from yardops import create_app
from yardops.extensions import db
from yardops.models.site import Site
from yardops.models.yard_spot import YardSpot
from yardops.models.trailer import Trailer
from config import TestingConfig

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def db_session(app):
    db.session.begin()
    yield db.session
    db.session.rollback()

@pytest.fixture
def sample_site(db_session):
    site = Site(name = "test site", address = "123")
    db_session.add(site)
    db_session.commit() 

    for i in range(4):
        spot = YardSpot(site_id = site.id,is_occupied = False)
        db_session.add(spot)
    db_session.commit()
    return site

@pytest.fixture
def drytrailer(db_session):
    trailer = Trailer(
        trailer_number = "123",
        trailer_type = "DRY",
        carrier_name = "test carrier"
    )
    db_session.add(trailer)
    db_session.commit()
    return trailer


    




