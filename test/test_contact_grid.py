import allure

from model.contact import Contact
from fixture.processing import merge_phones_like_on_home_page, merge_emails_like_on_home_page, clear_contact, \
    clear_spaces


def test_contact_grid_on_home_page(app, json_contacts, db):
    with allure.step("Given a non-empty contact list from UI"):
        if not db.get_contact_list():
            app.contact.create(json_contacts)
        contacts_from_home_page = app.contact.get_contact_list()
    with allure.step("Given a contact list from DB"):
        contacts_from_db = db.get_contact_list()
    # проверка списка полностью
    with allure.step("Then the contact lists are the same"):
        assert sorted(contacts_from_home_page, key=Contact.id_or_max) \
               == sorted(map(clear_contact, contacts_from_db), key=Contact.id_or_max)
    # если что-то падает, можно запустить детализированную и посмотреть
    with allure.step("Then the contact lastname, firstname, address, emails and phones "
                     "are the same for every contacts in both lists"):
        for i, contact in enumerate(sorted(contacts_from_home_page, key=Contact.id_or_max)):
            assert contact.lastname == clear_spaces(contacts_from_db[i].lastname)
            assert contact.firstname == clear_spaces(contacts_from_db[i].firstname)
            assert contact.address == clear_spaces(contacts_from_db[i].address)
            assert contact.all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
            assert contact.all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
