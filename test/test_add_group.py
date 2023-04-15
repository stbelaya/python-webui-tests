# -*- coding: utf-8 -*-
import allure
from fixture.processing import clear_group, clear_group_to_db
from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    with allure.step("Given a group list"):
        old_groups = db.get_group_list()
    with allure.step(f"When I add a group {group} to the list"):
        app.group.create(group)
    with allure.step("the new group list is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(clear_group_to_db(group))
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(map(clear_group, new_groups), key=Group.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.id_or_max)
