# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="sw00_01", header="sw00_head", footer="sw00_foot"))
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(group_name="", header="", footer=""))
    app.logout()



