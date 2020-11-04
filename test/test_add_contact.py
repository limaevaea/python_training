# -*- coding: utf-8 -*-
from model.contact import contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.fill_contact_form(
        contact(firstname="Limaeva", middlename="Ekaterina", lastname="Alexandrovna", nickname="kvakva", title="w",
                company="company123",
                address="Moscow mirovaya 1-23", home_telephone="8-999-999-12-12", email="testirovanie@mail.comcom",
                birth_date="16", birth_month="January",
                birth_year="1988"))
    app.session.logout()
