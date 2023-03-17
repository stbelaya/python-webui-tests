# -*- coding: utf-8 -*-
import os.path
import json
from model.group import Group
from generator.generation_helper import random_string, random_text
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    print(err)  # will print something like "option -a not recognized"
#    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


constant = [
    Group(name="sw00 name 1", header="sw00 header 1", footer="sw00 footer 1"),
    Group(name="sw00 name 2", header="sw00 header 2", footer="sw00 footer 2")
]

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_text("header", 20, 5), footer=random_text("footer", 20, 5))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
