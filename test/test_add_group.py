# -*- coding: utf-8 -*-
from fixture.group import clear_group
from model.group import Group
import pytest
from fixture.generation_helper import random_string, random_text


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_text("header", 20, 5), footer=random_text("footer", 20, 5))
    for i in range(5)
]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(clear_group(group))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



