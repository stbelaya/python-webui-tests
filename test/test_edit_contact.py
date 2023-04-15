# -*- coding: utf-8 -*-
import random
import allure

from model.contact import Contact
from fixture.processing import propagate, clear_contact


def test_edit_some_contact(app, json_contacts, db, check_ui):
    with allure.step("Given a non-empty contact list"):
        if not db.get_contact_list():
            app.contact.create(Contact(firstname="test"))
        old_contacts = db.get_contact_list()
    with allure.step("Given a random contact from the list"):
        contact = random.choice(old_contacts)
    new_contact = json_contacts
    new_contact.id = contact.id
    with allure.step(f"When I edit the contact {contact} from the list according to given contact {new_contact}"):
        app.contact.edit_contact_by_id(contact.id, new_contact)
    with allure.step("Then the new contact list is equal to the old list with the edited contact"):
        new_contacts = db.get_contact_list()
        old_contacts.remove(contact)
        old_contacts.append(propagate(contact, new_contact))
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            assert sorted(map(clear_contact, new_contacts), key=Contact.id_or_max) \
                   == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

