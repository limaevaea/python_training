# -*- coding: utf-8 -*-
from model.contact import contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    record = contact(firstname="Limaeva", middlename="Ekaterina", lastname="Alexandrovna", nickname="kvakva", title="w",
                company="company123",
                address="Moscow mirovaya 1-23", home="8-999-999-12-12", email="testirovanie@mail.comcom",
                birth_date="16", birth_month="January",
                birth_year="1988")
    app.contact.create_new_contact(record)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(record)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

