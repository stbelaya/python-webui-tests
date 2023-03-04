from selenium.webdriver.support.ui import Select
from model.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        if contact.photo is not None:
            wd.find_element_by_name("photo").send_keys(contact.photo)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("home", contact.home)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_dropdown_value("bday", contact.bday)
        self.change_dropdown_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_dropdown_value("aday", contact.aday)
        self.change_dropdown_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_dropdown_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("//input[@name='submit']").click()
        self.app.navigation.return_to_home_page()

    def edit_first(self, contact):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        # open contact modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # update contact form
        self.fill_form(contact)
        # submit contact edition
        wd.find_element_by_name("update").click()
        self.app.navigation.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        # WebDriverWait(wd, 5).until(ec.presence_of_element_located((By.ID, "MassCB")))
        wd.refresh()

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        contacts = []
        for element in wd.find_elements_by_css_selector("[name=entry]"):
            lastname = element.find_element_by_xpath("//td[2]").text
            firstname = element.find_element_by_xpath("//td[3]").text
            id = element.find_element_by_name("selected[]").get_attribute("id")
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return contacts
