# -*- coding: utf-8 -*-
import random
import allure

from model.contact import Contact
from fixture.processing import clear_contact_to_db
from model.group import Group


@allure.feature("Add contact to group")
@allure.description("User can add a random contact to a random group")
def test_add_contact_to_group(app, db):
    with allure.step("Given a non-empty group list"):
        groups = db.get_group_list()
        if not groups:
            app.group.create(Group(name="group test"))
            groups = db.get_group_list()
    with allure.step("Given a random group from the list"):
        group = random.choice(groups)
    with allure.step("Given a non-empty contact list for contacts without groups"):
        contacts = db.get_contacts_not_in_group(group)
        if not contacts:
            app.contact.create(Contact(firstname="First test1", lastname="Last test1"))
            contacts = db.get_contacts_not_in_group(group)
    with allure.step("Given a random contact from the list"):
        contact = random.choice(contacts)
    with allure.step(f"When I add the contact {contact} to the group {group}"):
        app.contact.add_contact_to_group(contact.id, group.id)
    with allure.step("Then the contact is in the group"):
        assert clear_contact_to_db(contact) in db.get_contacts_in_group(group), "Contact is not added to the group"
