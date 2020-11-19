from model.group import Group
from random import randrange

def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Edit Name"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Edit Name")
    group.id = old_groups[index].id
    app.group.edit_some_group(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)