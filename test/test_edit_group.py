# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="Updated name", header="Updated header", footer="Updated footer")
    group.id = old_groups[0].id
    app.group.edit_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# def test_edit_first_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(name="Updated name2"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#
#
# def test_edit_first_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first(Group(header="Updated header3"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
