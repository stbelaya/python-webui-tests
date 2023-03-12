# -*- coding: utf-8 -*-
from fixture.generation_helper import random_string, random_text
from model.contact import Contact
import pytest
import random
import calendar
from fixture.contact import clear_contact


def random_day():
    return str(random.randrange(1, 31))


def random_month():
    return calendar.month_name[random.randrange(1, 12)]


def random_year():
    return str(random.randrange(1, 9999))


testdata = [Contact(firstname="", middlename="", lastname="")] + [
    Contact(firstname="Svetlana", middlename="Borisovna", lastname="Kovaleva",
            nickname="Belaya",
            title="Tester", company="The Best",
            address="Lenina, 8", mobile="89001001213", home="555555", work="121212",
            fax="111111", email="stbelaya@gmail.com", email2="stbelaya2@gmail.com",
            email3="stbelaya3@gmail.com", homepage="google.com", bday="13",
            bmonth="October", byear="1985", aday="31", amonth="December",
            ayear="2023", address2="Sokolovka, 22", phone2="89002222222",
            notes="заметка")
] + [
    Contact(firstname=random_string("name", 20), middlename=random_string("middle", 20),
            lastname=random_string("lastname", 20), nickname=random_string("nick", 20),
            title=random_string("title", 25), company=random_string("company", 30),
            address=random_text("address", 50, 10), mobile=random_string("mobile", 11),
            home=random_string("home", 11), work=random_string("work", 11),
            fax=random_string("fax", 20), email=random_string("email", 20),
            email2=random_string("email2", 20), email3=random_string("email3", 20),
            homepage=random_string("homepage", 20), bday=random_day(), bmonth=random_month(),
            byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
            address2=random_text("address2", 50, 10), phone2=random_string("phone2", 20),
            notes=random_text("notes", 50, 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert app.contact.count() == len(old_contacts) + 1
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(clear_contact(contact))
    assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)

