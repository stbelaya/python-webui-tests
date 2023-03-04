# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Svetlana", middlename="Borisovna", lastname="Kovaleva")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_full_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="Svetlana", middlename="Borisovna", lastname="Kovaleva",
#                                nickname="Belaya",
#                                title="Tester", company="The Best",
#                                address="Lenina, 8", mobile="89001001213", home="555555", work="121212",
#                                fax="111111", email="stbelaya@gmail.com", email2="stbelaya2@gmail.com",
#                                email3="stbelaya3@gmail.com", homepage="google.com", bday="13",
#                                bmonth="October", byear="1985", aday="31", amonth="December",
#                                ayear="2023", address2="Sokolovka, 22", phone2="89002222222",
#                                notes="заметка")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

# def test_add_empty_contact(app):
#     app.contact.create(Contact())
