from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By


class NavigationHelper:

    def __init__(self, app, base_url):
        self.app = app
        self.home_page = base_url
        self.groups_page = "/group.php"
        self.group_page = "/?group="

    def open_home_page(self):
        wd = self.app.wd
        home_page = self.home_page
        if self.is_on_page(home_page, "searchstring") is False or ec.alert_is_present() is True:
            wd.get(home_page)

    def return_to_home_page(self):
        wd = self.app.wd
        home_page = self.home_page
        if ec.alert_is_present() is True:
            wd.switch_to.alert.dismiss()
        elif self.is_on_page(home_page, "searchstring") is False:
            wd.find_element(By.LINK_TEXT, "home page").click()

    def is_on_page(self, url, element):
        wd = self.app.wd
        return wd.current_url.endswith(url) and len(wd.find_elements(By.NAME, element)) > 0

    def open_groups_page(self):
        wd = self.app.wd
        groups_page = self.groups_page
        if self.is_on_page(groups_page, "new") is False:
            wd.find_element(By.LINK_TEXT, "groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        groups_page = self.groups_page
        if self.is_on_page(groups_page, "new") is False:
            wd.find_element(By.LINK_TEXT, "group page").click()

    def go_to_group_page(self, id):
        wd = self.app.wd
        group_page = self.group_page + id
        if self.is_on_page(group_page, "group") is False:
            wd.find_element(By.PARTIAL_LINK_TEXT, "group page").click()
