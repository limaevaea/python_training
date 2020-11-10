from model.contact import contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact(firstname="AddNewContact"))
    app.contact.delete_first_contact()
