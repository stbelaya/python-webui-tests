# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Svetlana", middlename="Borisovna", lastname="Kovaleva",
                       nickname="Belaya",
                       photo="C:\\Sync\\YandexDisk\\FoldersForWindows\\Pictures\\LogoLP.jpg",
                       title="Tester", company="The Best",
                       address="Lenina, 8", mobile="89001001213", home="555555", work="121212",
                       fax="111111", email="stbelaya@gmail.com", email2="stbelaya2@gmail.com",
                       email3="stbelaya3@gmail.com", homepage="google.com", bday="13",
                       bmonth="October", byear="1985", aday="31", amonth="December",
                       ayear="2023", address2="Sokolovka, 22", phone2="89002222222",
                       notes="заметка"))
    app.session.logout()
