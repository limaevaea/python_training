# -*- coding: utf-8 -*-
from model.contact import contact


def test_add_contact(app):
    app.contact.create_new_contact(
        contact(firstname="Limaeva", middlename="Ekaterina", lastname="Alexandrovna", nickname="kvakva", title="w",
                company="company123",
                address="Moscow mirovaya 1-23", home="8-999-999-12-12", email="testirovanie@mail.comcom",
                birth_date="16", birth_month="January",
                birth_year="1988"))

