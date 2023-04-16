import allure

from fixture.processing import clear_group
from model.group import Group


@allure.feature("Group list on the group page")
@allure.description("Check that group data from the group page is displayed accordingly to group data from DB")
def test_group_list(app, db):
    with allure.step("Given a non-empty group list from UI"):
        if not app.group.get_group_list():
            app.group.create(Group(name="group test"))
        ui_list = app.group.get_group_list()
    with allure.step("Given a group list from DB"):
        db_list = db.get_group_list()
    with allure.step("Then the group lists are the same"):
        assert sorted(ui_list, key=Group.id_or_max) == sorted(map(clear_group, db_list), key=Group.id_or_max)
