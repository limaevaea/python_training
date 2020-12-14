from model.сontact import Сontact
import random

def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Сontact(middlename="Ekaterina", lastname="Alexandrovna"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    record = Сontact(firstname="Testing01", lastname="Testing01") #  middlename="Testing01", nickname="Testing01", title="w",
                #company="Testing01", address="Moscow mirovaya 1-23", birth_year="2019"
    app.contact.edit_some_contact_by_id(contact.id, record)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Сontact.id_or_max) == sorted(new_contacts, key=Сontact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Сontact.id_or_max) == sorted(app.contact.get_contact_list(), key=Сontact.id_or_max)
