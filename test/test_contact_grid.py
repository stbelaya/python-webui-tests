from random import randrange
from generator.generation_helper import random_string, clear_spaces
from model.contact import Contact
from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page


def test_contact_grid_on_home_page(app, json_contacts):
    if app.contact.count() == 0:
        app.contact.create(json_contacts)
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == clear_spaces(contact_from_edit_page.lastname)
    assert contact_from_home_page.firstname == clear_spaces(contact_from_edit_page.firstname)
    assert contact_from_home_page.address == clear_spaces(contact_from_edit_page.address)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
