# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="sw00_01", header="sw00_head", footer="sw00_foot"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(group_name="", header="", footer=""))
    app.session.logout()



