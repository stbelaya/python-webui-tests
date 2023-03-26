import random
from fixture.processing import clear_contact
from model.contact import Contact


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="First_test", lastname="Last_test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(map(clear_contact, new_contacts), key=Contact.id_or_max) \
               == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
