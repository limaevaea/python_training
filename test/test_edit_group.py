from model.group import Group

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="NewTest000001"))
    app.group.edit_first_group(Group(name="Edit Name"))
