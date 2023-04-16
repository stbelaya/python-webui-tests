*** Settings ***
Library  Collections
Library  rf\AddressBook.py
Library  rf\LoginLibrary.py
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures


*** Test Cases ***
Add new group
    $(old_list)=  Get Group List
    $(group)=  New Group  name1  header1  footer1
    Create Group  $(group)
    $(new_list)=  Get Group List
    Append To List    $(old_list)  $(group)
    Group Lists Should be Equal  $(new_list)  $(old_list)