from random import randrange, choice
import string
from model.contact import Contact
from fixture.contact import merge_emails_like_on_home_page, merge_phones_like_on_home_page


def test_contact_grid_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(
            firstname="".join([choice(string.ascii_letters + string.digits) for i in range(randrange(20))]),
            lastname="".join([choice(string.ascii_letters + string.digits) for i in range(randrange(20))]),
            address="".join([choice(string.ascii_letters + string.digits + " .-") for i in range(randrange(50))]),
            email="".join([choice(string.ascii_letters + string.digits) for i in range(randrange(20))]),
            email2="".join([choice(string.ascii_letters + string.digits) for i in range(randrange(20))]),
            email3="".join([choice(string.ascii_letters + string.digits) for i in range(randrange(20))]),
            home="".join([choice(string.digits + "+ - ()") for i in range(randrange(15))]),
            mobile="".join([choice(string.digits + "+ - ()") for i in range(randrange(15))]),
            work="".join([choice(string.digits + "+ - ()") for i in range(randrange(15))]),
            phone2="".join([choice(string.digits + "+ - ()") for i in range(randrange(15))])
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
