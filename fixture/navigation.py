from selenium.webdriver.support import expected_conditions as ec


class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.wd
        if self.is_on_page("localhost/addressbook/", "searchstring") is False or ec.alert_is_present() is True:
            wd.get("https://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.app.wd
        if ec.alert_is_present() is True:
            wd.switch_to.alert.dismiss()
        elif self.is_on_page("localhost/addressbook/", "searchstring") is False:
            wd.find_element_by_link_text("home page").click()

    def is_on_page(self, url, element):
        wd = self.app.wd
        return wd.current_url.endswith(url) and len(wd.find_elements_by_name(element)) > 0

    def open_groups_page(self):
        wd = self.app.wd
        if self.is_on_page("/group.php", "new") is False:
            wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        if self.is_on_page("/group.php", "new") is False:
            wd.find_element_by_link_text("group page").click()
