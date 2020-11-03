# -*- coding: utf-8 -*-
from model.group import Group


def test_add_new_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="NewTest01", header="Testing1", footer="Test"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()



