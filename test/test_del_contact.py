from model.contact import contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact(firstname="AddNewContact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
