# -*- coding: utf-8 -*-
import random
import allure

from model.contact import Contact
from fixture.processing import clear_contact_to_db
from model.group import Group


def test_del_contact_from_group(app, db):
    with allure.step("Given a non-empty group list"):
        groups = db.get_group_list()
        if not groups:
            app.group.create(Group(name="group test"))
            groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        group = random.choice(groups)
    with allure.step(f"Given a non-empty contact list for contacts in the group {group}"):
        contacts = db.get_contacts_in_group(group)
        if not contacts:
            app.contact.create(Contact(firstname="First test1", lastname="Last test1"))
            contacts = db.get_contact_list()
            app.contact.add_contact_to_group(contacts[0].id, group.id)
            contacts = db.get_contacts_in_group(group)
    with allure.step("Given a random contact from the list"):
        contact = random.choice(contacts)
    with allure.step(f"When I remove the contact {contact} from the group {group}"):
        app.contact.remove_contact_from_group(contact.id, group.id)
    with allure.step("Then the contact is not in the group"):
        assert clear_contact_to_db(contact) in db.get_contacts_not_in_group(group)
