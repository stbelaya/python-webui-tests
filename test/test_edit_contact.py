# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="updSvetlana", middlename="updBorisovna", lastname="updKovaleva",
                       nickname="updBelaya",
                       title="updTester", company="updThe Best",
                       address="updLenina, 8", mobile="upd89001001213", home="upd555555", work="upd121212",
                       fax="upd111111", email="updstbelaya@gmail.com", email2="updstbelaya2@gmail.com",
                       email3="updstbelaya3@gmail.com", homepage="updgoogle.com", bday="1",
                       bmonth="January", byear="1999", aday="30", amonth="November",
                       ayear="2020", address2="updSokolovka, 22", phone2="upd89002222222",
                       notes="updзаметка"))
    app.session.logout()


def test_edit_first_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Anakin"))
    app.session.logout()
