# -*- coding: utf-8 -*-
from model.contact import Contact
from fixture.contact import clear_contact


def test_add_contact(app, json_contacts):
    contact = json_contacts
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(clear_contact(contact))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

