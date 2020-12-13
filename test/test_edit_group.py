from model.group import Group
import random

def test_edit_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Edit Name"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    rename = Group(name="Edit Name")
    app.group.edit_group_by_id(group.id, rename)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
