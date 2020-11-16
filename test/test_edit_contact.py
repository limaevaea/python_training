from model.contact import contact

def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create_new_contact(contact(middlename="Ekaterina", lastname="Alexandrovna"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(
        contact(firstname="Testing01", middlename="Testing01", lastname="", nickname="Testing01", title="w",
                company="Testing01", address="Moscow mirovaya 1-23", birth_year="2019"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
