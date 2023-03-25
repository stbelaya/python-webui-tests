from selenium.webdriver.support.ui import Select
from generator.generation_helper import clear_spaces, clear_spaces_textarea
from model.contact import Contact
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import re


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
            Select(wd.find_element(By.NAME, field_name)).select_by_visible_text(text)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init contact creation
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        self.fill_form(contact)
        # submit contact creation
        wd.find_element(By.CSS_SELECTOR, "input[name='submit']").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # update contact form
        self.fill_form(contact)
        # submit contact edition
        wd.find_element(By.NAME, "update").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # update contact form
        self.fill_form(contact)
        # submit contact edition
        wd.find_element(By.NAME, "update").click()
        self.app.navigation.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, "img[alt='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element(By.CSS_SELECTOR, f"a[href='edit.php?id={id}']").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, "img[alt='Details']")[index].click()

    def edit_first(self, contact):
        self.edit_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        # select first contact
        wd.find_elements(By.NAME, "selected[]")[index].click()
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        # select contact with id
        wd.find_element(By.CSS_SELECTOR, f"input[value='{id}']").click()
        # submit deletion
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete']").click()
        wd.switch_to.alert.accept()
        WebDriverWait(wd, 5).until(ec.presence_of_element_located((By.CSS_SELECTOR, "div.msgbox")))
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.navigation.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements(By.NAME, "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                id = row.find_element(By.NAME, "selected[]").get_attribute("id")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobilephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        workphone = wd.find_element(By.NAME, "work").get_attribute("value")
        secondaryphone = wd.find_element(By.NAME, "phone2").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, home=homephone,
                       mobile=mobilephone, work=workphone, phone2=secondaryphone, address=address,
                       email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        firstname = wd.find_element(By.TAG_NAME, "b").text.split(" ")[0]
        lastname = wd.find_element(By.TAG_NAME, "b").text.split(" ")[-1]
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(firstname=firstname, lastname=lastname, id=id, home=homephone,
                       mobile=mobilephone, work=workphone, phone2=secondaryphone)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def clear_phone(s):
    return re.sub("[/.() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                            [clear_spaces(contact.email), clear_spaces(contact.email2), clear_spaces(contact.email3)]))


def clear_contact(contact):
    _ = clear_spaces
    __ = clear_spaces_textarea
    return Contact(firstname=_(contact.firstname), middlename=contact.middlename,
                   lastname=_(contact.lastname), nickname=contact.nickname,
                   title=contact.title, company=contact.company,
                   address=__(contact.address), mobile=_(contact.mobile),
                   home=_(contact.home), work=_(contact.work),
                   fax=_(contact.fax), email=_(contact.email),
                   email2=_(contact.email2), email3=_(contact.email3),
                   homepage=contact.homepage, bday=contact.bday, bmonth=contact.bmonth,
                   byear=contact.byear, aday=contact.aday, amonth=contact.amonth, ayear=contact.ayear,
                   address2=contact.address2, phone2=_(contact.phone2),
                   notes=contact.notes, id=contact.id,
                   all_emails_from_home_page=merge_emails_like_on_home_page(contact),
                   all_phones_from_home_page=merge_phones_like_on_home_page(contact))
