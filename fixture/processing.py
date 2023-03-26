import re

from model.contact import Contact
from model.group import Group


def propagate(data_source, obj):
    for key, value in data_source.__dict__.items():
        if getattr(obj, key) is None:
            setattr(obj, key, value)
    return obj


def clear_to_db(s):
    return "" if s is None else s


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_phone(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.mobile, contact.work, contact.phone2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x is not None and x != "",
                            [clear_spaces(contact.email), clear_spaces(contact.email2), clear_spaces(contact.email3)]))


def clear_phone(s):
    return re.sub("[/.() -]", "", s)


def clear_contact(contact):
    _ = clear_spaces
    __ = clear_spaces_textarea
    return Contact(firstname=_(contact.firstname), middlename=contact.middlename,
                   lastname=_(contact.lastname), nickname=contact.nickname,
                   title=contact.title, company=contact.company,
                   address=__(contact.address), mobile=_(contact.mobile),
                   home=_(contact.home), work=_(contact.work),
                   fax=_(contact.fax), email=_(contact.email),
                   email2=_(contact.email2), email3=_(contact.email3),
                   homepage=contact.homepage, bday=contact.bday, bmonth=contact.bmonth,
                   byear=contact.byear, aday=contact.aday, amonth=contact.amonth, ayear=contact.ayear,
                   address2=contact.address2, phone2=_(contact.phone2),
                   notes=contact.notes, id=contact.id,
                   all_emails_from_home_page=merge_emails_like_on_home_page(contact),
                   all_phones_from_home_page=merge_phones_like_on_home_page(contact))


def clear_contact_to_db(contact):
    _ = clear_to_db
    return Contact(firstname=_(contact.firstname), middlename=contact.middlename,
                   lastname=_(contact.lastname), nickname=contact.nickname,
                   title=contact.title, company=contact.company,
                   address=_(contact.address), mobile=_(contact.mobile),
                   home=_(contact.home), work=_(contact.work),
                   fax=_(contact.fax), email=_(contact.email),
                   email2=_(contact.email2), email3=_(contact.email3),
                   homepage=contact.homepage, bday=contact.bday, bmonth=contact.bmonth,
                   byear=contact.byear, aday=contact.aday, amonth=contact.amonth, ayear=contact.ayear,
                   address2=contact.address2, phone2=_(contact.phone2),
                   notes=contact.notes, id=contact.id,
                   all_emails_from_home_page=contact.all_emails_from_home_page,
                   all_phones_from_home_page=contact.all_phones_from_home_page)


def clear_group(group):
    _ = clear_spaces
    return Group(id=group.id, name=_(group.name), header=_(group.header), footer=_(group.footer))


def clear_group_to_db(group):
    _ = clear_to_db
    return Group(id=group.id, name=_(group.name), header=_(group.header), footer=_(group.footer))


def clear_spaces(s):
    return " ".join(s.split()) if s is not None else ""


def clear_spaces_textarea(s):
    return re.sub(" +", " ", re.sub(" \n", "\n", re.sub("\n ", "\n", s))).strip() if s is not None else ""
