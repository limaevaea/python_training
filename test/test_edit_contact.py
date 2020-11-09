from model.contact import contact

def test_edit_first_contact(app):
    app.contact.edit_first_contact(
        contact(firstname="Testing01", middlename="Testing01", lastname="", nickname="Testing01", title="w",
                company="Testing01", address="Moscow mirovaya 1-23", birth_year="2019"))
