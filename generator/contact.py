from generator.generation_helper import random_year, random_month, random_day, random_string, random_text
import os.path
import jsonpickle
from model.contact import Contact
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    print(err)  # will print something like "option -a not recognized"
    #    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

constant = [
           Contact(firstname="", middlename="", lastname="")] + [
           Contact(firstname=" ", middlename=" ", lastname=" ")] + [
           Contact(firstname="Svetlana", middlename="Borisovna", lastname="Kovaleva",
                   nickname="Belaya",
                   title="Tester", company="The Best",
                   address="Lenina, 8", mobile="89001001213", home="555555", work="121212",
                   fax="111111", email="stbelaya@gmail.com", email2="stbelaya2@gmail.com",
                   email3="stbelaya3@gmail.com", homepage="google.com", bday="13",
                   bmonth="October", byear="1985", aday="31", amonth="December",
                   ayear="2023", address2="Sokolovka, 22", phone2="89002222222",
                   notes="заметка")
       ]

testdata = [
            Contact(firstname="", middlename="", lastname="", address="", email="", email2="",
                    email3="", mobile="", home="", work="", phone2="")] + [
            Contact(firstname=" ", middlename=" ", lastname=" ", address=" ", email=" ", email2=" ",
                    email3=" ", mobile=" ", home=" ", work=" ", phone2=" ")] + [
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
            for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
