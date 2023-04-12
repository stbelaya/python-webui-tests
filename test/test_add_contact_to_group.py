# -*- coding: utf-8 -*-
import random

from model.contact import Contact
from fixture.processing import clear_contact_to_db
from model.group import Group


def test_add_contact_to_group(app, db):
    groups = db.get_group_list()
    if not groups:
        app.group.create(Group(name="group test"))
        groups = db.get_group_list()
    group = random.choice(groups)
    contacts = db.get_contacts_not_in_group(group)
    if not contacts:
        app.contact.create(Contact(firstname="First test1", lastname="Last test1"))
        contacts = db.get_contacts_not_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact.id, group.id)
    assert clear_contact_to_db(contact) in db.get_contacts_in_group(group)
