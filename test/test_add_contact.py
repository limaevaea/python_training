# -*- coding: utf-8 -*-
from model.contact import contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    record = contact(firstname="Limaeva1", middlename="Ekaterina", lastname="Alexandrovna", nickname="kvakva", title="w",
                company="company123",
                address="Moscow mirovaya 1-23", home="8-912-854-854", mobile="12345", work="2345", email="testirovanie@mail.comcom",
                birth_date="16", birth_month="January", birth_year="1988")
    app.contact.create_new_contact(record)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(record)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

