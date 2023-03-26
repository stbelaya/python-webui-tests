# -*- coding: utf-8 -*-
import random
from model.contact import Contact
from fixture.processing import propagate, clear_contact


def test_edit_some_contact(app, json_contacts, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    new_contact = json_contacts
    new_contact.id = contact.id
    app.contact.edit_contact_by_id(contact.id, new_contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    old_contacts.append(propagate(contact, new_contact))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(clear_contact, new_contacts), key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

