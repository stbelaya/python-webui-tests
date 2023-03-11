from random import randrange, choice
import string
from model.contact import Contact
from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_contact_grid_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname=random_string("name", 15),
            lastname=random_string("lastname", 15),
            address=random_string("address", 50),
            email=random_string("email", 15),
            email2=random_string("email2", 15),
            email3=random_string("email3", 15),
            home=random_string("home", 10),
            mobile=random_string("mobile", 10),
            work=random_string("work", 10),
            phone2=random_string("phone2", 10)
        ))
    all_contacts = app.contact.get_contact_list()
    index = randrange(len(all_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
