from model.сontact import Сontact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(Сontact(middlename="Ekaterina", lastname="Alexandrovna"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    record = Сontact(firstname="Testing01", lastname="Testing01") #  middlename="Testing01", nickname="Testing01", title="w",
                #company="Testing01", address="Moscow mirovaya 1-23", birth_year="2019"
    record.id = old_contacts[index].id
    app.contact.edit_some_contact(index, record)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = record
    assert sorted(old_contacts, key=Сontact.id_or_max) == sorted(new_contacts, key=Сontact.id_or_max)