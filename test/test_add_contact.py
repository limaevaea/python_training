# -*- coding: utf-8 -*-
import pytest
from model.contact import contact
from fixture.contact_application import Contact_application


@pytest.fixture
def cont_app(request):
    fixture = Contact_application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(cont_app):
    cont_app.session_contact.login(username="admin", password="secret")
    cont_app.fill_contact_form(
        contact(firstname="Limaeva", middlename="Ekaterina", lastname="Alexandrovna", nickname="kvakva", title="w",
                company="company123",
                address="Moscow mirovaya 1-23", home_telephone="8-999-999-12-12", email="testirovanie@mail.comcom",
                birth_date="16", birth_month="January",
                birth_year="1988"))
    cont_app.session_contact.logout()
