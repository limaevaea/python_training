import pytest
from fixture.application import Application
from fixture.contact_application import Contact_application


@pytest.fixture(scope="session")
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

@pytest.fixture(scope="session")
def cont_app(request):
    fixture = Contact_application()
    request.addfinalizer(fixture.destroy)
    return fixture