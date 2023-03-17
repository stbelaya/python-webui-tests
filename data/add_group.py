# -*- coding: utf-8 -*-
from model.group import Group
from data.generation_helper import random_string, random_text


constant = [
    Group(name="sw00 name 1", header="sw00 header 1", footer="sw00 footer 1"),
    Group(name="sw00 name 2", header="sw00 header 2", footer="sw00 footer 2")
]

testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_text("header", 20, 5), footer=random_text("footer", 20, 5))
    for i in range(5)
]