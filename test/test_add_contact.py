# -*- coding: utf-8 -*-
from model.contact import contact
import pytest
import random #выбираем случано
import string #содержит константы списки символов

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    contact(firstname="", middlename="Ekaterina", lastname="")] + [
    contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10), nickname=random_string("lastname", 10), title="w",
    company="company123",address="Moscow mirovaya 1-23", home="8-912-854-854", mobile="12345", work="2345", email="testirovanie@mail.comcom",
    birth_date="16", birth_month="January", birth_year="1988")
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)

