import random
import allure

from model.group import Group
from fixture.processing import clear_group


def test_delete_some_group(app, db, check_ui):
    with allure.step("Given a non-empty group list"):
        if not db.get_group_list():
            app.group.create(Group(name="test"))
        old_groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        group = random.choice(old_groups)
    with allure.step(f"When I delete the group {group} from the list"):
        app.group.delete_group_by_id(group.id)
    with allure.step("Then the new group list is equal to the old list without the deleted group"):
        assert len(old_groups) - 1 == app.group.count()
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(map(clear_group, new_groups), key=Group.id_or_max) == \
                   sorted(app.group.get_group_list(), key=Group.id_or_max)
