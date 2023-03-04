# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="updSvetlana", middlename="updBorisovna", lastname="updKovaleva")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_full_first_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="updSvetlana", middlename="updBorisovna", lastname="updKovaleva",
#                        nickname="updBelaya",
#                        title="updTester", company="updThe Best",
#                        address="updLenina, 8", mobile="upd89001001213", home="upd555555", work="upd121212",
#                        fax="upd111111", email="updstbelaya@gmail.com", email2="updstbelaya2@gmail.com",
#                        email3="updstbelaya3@gmail.com", homepage="updgoogle.com", bday="1",
#                        bmonth="January", byear="1999", aday="30", amonth="November",
#                        ayear="2020", address2="updSokolovka, 22", phone2="upd89002222222",
#                        notes="updзаметка")
#     app.contact.edit_first(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#     old_contacts[0] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_edit_first_contact_firstname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="test"))
#     app.contact.edit_first(Contact(firstname="Anakin"))
