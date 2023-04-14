from pytest_bdd import given, when, then, parsers

from fixture.processing import clear_contact, clear_contact_to_db, propagate
from model.contact import Contact


@given("a contact list", target_fixture="contact_list")
def contact_list(db):
    return db.get_contact_list()


@given(parsers.parse("a contact with {firstname}, {lastname}, {address}, {email} and {mobile}"),
       target_fixture="new_contact")
def new_contact(firstname, lastname, address, email, mobile):
    return Contact(firstname=firstname, lastname=lastname, address=address, email=email, mobile=mobile)


@when("I add the contact to the list")
def add_new_contact(app, new_contact):
    app.contact.create(new_contact)


@then("the new contact list is equal to the old list with the added contact")
def verify_contact_added(app, db, contact_list, new_contact, check_ui):
    old_contacts = contact_list
    new_contacts = db.get_contact_list()
    old_contacts.append(clear_contact_to_db(new_contact))
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(map(clear_contact, new_contacts), key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)