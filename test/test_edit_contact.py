from model.contact import contact

def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(
        contact(firstname="Testing01", middlename="Testing01", lastname="", nickname="Testing01", title="w",
                company="Testing01",
                address="Moscow mirovaya 1-23", home_telephone="8-999-999-12-12", email="Testing01@mail.comcom",
                birth_date="16", birth_month="March",
                birth_year="2019"))
    app.session.logout()