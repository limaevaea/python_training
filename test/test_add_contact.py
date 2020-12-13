# -*- coding: utf-8 -*-
from model.сontact import Сontact

def test_add_contact(app, db, json_contacts):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create_new_contact(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Сontact.id_or_max) == sorted(new_contacts, key=Сontact.id_or_max)


