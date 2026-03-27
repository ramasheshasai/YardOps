import pytest
from yardops import create_app
from yardops.extensions import db
from yardops.models.site import Site
from yardops.models.yard_spot import YardSpot
from yardops.models.trailer import Trailer
from config import TestingConfig
from yardops.extensions import redis_client

@pytest.fixture(scope="function")
def app():
    app = create_app(TestingConfig)

    ctx = app.app_context()
    ctx.push()   

    db.create_all()

    yield app

    db.session.remove()
    db.drop_all()
    ctx.pop()  

@pytest.fixture(autouse=True)
def clear_redis():
    redis_client.flushall()

@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():   
            yield client

@pytest.fixture
def sample_site(app):
    site = Site(name = "test site", address = "123")
    db.session.add(site)
    db.session.commit() 

    for i in range(4):
        spot = YardSpot(
            site_id = site.id,
            is_occupied = False,
            spot_label = f"Spot {i+1}"
        )
        db.session.add(spot)
    db.session.commit()
    db.session.refresh(site)
    return site

@pytest.fixture
def drytrailer(app):
    trailer = Trailer(
        trailer_number = "123",
        trailer_type = "DRY",
        carrier_name = "test carrier"
    )
    db.session.add(trailer)
    db.session.commit()
    return trailer
