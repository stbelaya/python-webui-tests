# -*- coding: utf-8 -*-
import random
from fixture.processing import propagate, clear_group
from model.group import Group


def test_edit_some_group(app, json_groups, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    new_group = json_groups
    new_group.id = group.id
    app.group.edit_group_by_id(group.id, new_group)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    old_groups.append(propagate(group, new_group))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(clear_group, new_groups), key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)
