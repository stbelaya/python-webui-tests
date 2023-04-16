# -*- coding: utf-8 -*-
import allure

from model.contact import Contact
from fixture.processing import clear_contact, clear_contact_to_db


@allure.feature("Add contact")
@allure.description("User can add a new contact with empty fields, space fields, random generated fields")
def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    with allure.step("Given a contact list"):
        old_contacts = db.get_contact_list()
    with allure.step(f"When I add the contact {contact} to the list"):
        app.contact.create(contact)
    with allure.step("Then the new contact list is equal to the old list with the added contact"):
        new_contacts = db.get_contact_list()
        old_contacts.append(clear_contact_to_db(contact))
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(map(clear_contact, new_contacts), key=Contact.id_or_max) == \
                   sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
