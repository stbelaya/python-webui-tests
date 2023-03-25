import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                lst.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return lst

    def get_contact_list(self):
        lst = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3"
                           " FROM addressbook WHERE deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3) = row
                lst.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                   mobile=mobile, home=home, work=work, phone2=phone2,
                                   email=email, email2=email2, email3=email3))
        finally:
            cursor.close()
        return lst

    def destroy(self):
        self.connection.close()
