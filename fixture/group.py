from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill group form
        self.fill_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_id(id)
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def edit_first(self, group):
        self.edit_group_by_index(0, group)

    def edit_group_by_index(self, index, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_index(index)
        # submit edition
        wd.find_element(By.NAME, "edit").click()
        # update group form
        self.fill_form(group)
        # submit group creation
        wd.find_element(By.NAME, "update").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, group):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        self.select_group_by_id(id)
        # submit edition
        wd.find_element(By.NAME, "edit").click()
        # update group form
        self.fill_form(group)
        # submit group creation
        wd.find_element(By.NAME, "update").click()
        self.app.navigation.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, f"input[value='{id}']").click()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.app.navigation.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))

        return list(self.group_cache)
