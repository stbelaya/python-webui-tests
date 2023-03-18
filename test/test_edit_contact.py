# -*- coding: utf-8 -*-
from generator.generation_helper import clear_spaces
from model.contact import Contact
from random import randrange
from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page, clear_contact


def test_edit_some_contact(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = json_contacts
    contact.all_emails_from_home_page = merge_emails_like_on_home_page(contact)
    contact.all_phones_from_home_page = merge_phones_like_on_home_page(contact)
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = clear_contact(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

