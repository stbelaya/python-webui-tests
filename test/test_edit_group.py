# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first(Group(name="Updated name", header="Updated header", footer="Updated footer"))


def test_edit_first_group_name(app):
    app.group.edit_first(Group(name="Updated name2"))


def test_edit_first_group_header(app):
    app.group.edit_first(Group(header="Updated header3"))
