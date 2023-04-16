# -*- coding: utf-8 -*-
import random
import allure

from fixture.processing import propagate, clear_group
from model.group import Group


@allure.feature("Edit random group")
@allure.description("User can edit a random group to have empty fields, space fields, random generated fields")
def test_edit_some_group(app, json_groups, db, check_ui):
    with allure.step("Given a non-empty group list"):
        if not db.get_group_list():
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        group = random.choice(old_groups)
    new_group = json_groups
    new_group.id = group.id
    with allure.step(f"When I edit the group {group} in the list according to given group {new_group}"):
        app.group.edit_group_by_id(group.id, new_group)
    with allure.step("Then the new group list is equal to the old list with the edited group"):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        old_groups.append(propagate(group, new_group))
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            assert sorted(map(clear_group, new_groups), key=Group.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.id_or_max)
