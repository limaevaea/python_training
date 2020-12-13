from model.сontact import Сontact
import random

def test_delete_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new_contact(Сontact(firstname="AddNewContact"))
    old_contacts = db.get_contact_list()
    contact =random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id) #переделать метод новый
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact) #вырезка от 0 до 1 не вкл 1
    assert old_contacts == new_contacts
