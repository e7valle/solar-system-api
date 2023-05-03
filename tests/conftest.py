import pytest
from app import create_app, db
from app.models.solar_system import Planet
from flask.signals import request_finished

@pytest.fixture
def app():
    app = create_app(testing=True)

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app
    
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def two_planets():
    mars = Planet(name="Mars", description="Fourth planet from the Sun", moons=2, color="Brown")
    venus = Planet(name="Venus", description="Second planet from the Sun", moons=0, color="Orange")

    db.session.add_all([mars, venus])
    db.session.commit()

