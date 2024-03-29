from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, photo=None, title=None,
                 company=None, address=None,
                 mobile=None, home=None, work=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 bday=None, bmonth=None,
                 byear=None, aday=None, amonth=None, ayear=None, address2=None, phone2=None, notes=None, id=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.mobile = mobile
        self.home = home
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return f"{self.id}: {self.firstname}; {self.lastname}; {self.address}; " \
               f"{self.all_emails_from_home_page}; {self.all_phones_from_home_page}"

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.firstname == other.firstname and self.lastname == other.lastname \
            and self.address == other.address \
            and self.all_emails_from_home_page == other.all_emails_from_home_page \
            and self.all_phones_from_home_page == other.all_phones_from_home_page

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
