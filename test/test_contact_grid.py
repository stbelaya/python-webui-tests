from random import randrange
from generator.generation_helper import random_string, clear_spaces
from model.contact import Contact
from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page, clear_contact


def test_contact_grid_on_home_page(app, json_contacts, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(json_contacts)
    contacts_from_home_page = app.contact.get_contact_list()
    contacts_from_db = db.get_contact_list()
    # проверка списка полностью
    assert sorted(contacts_from_home_page, key=Contact.id_or_max) \
           == sorted(map(clear_contact, contacts_from_db), key=Contact.id_or_max)
    # если что-то падает, можно запустить детализированную и посмотреть
    for i, contact in enumerate(sorted(contacts_from_home_page, key=Contact.id_or_max)):
        assert contact.lastname == clear_spaces(contacts_from_db[i].lastname)
        assert contact.firstname == clear_spaces(contacts_from_db[i].firstname)
        assert contact.address == clear_spaces(contacts_from_db[i].address)
        assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
        assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
