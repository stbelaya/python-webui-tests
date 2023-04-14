from pytest_bdd import scenario

from .contact_steps import *


@scenario("contacts.feature", "Add new contact")
def test_add_new_contact():
    pass
