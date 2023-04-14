Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>, <email> and <mobile>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact


  Examples:
  | firstname  | lastname  | address  | email | mobile  |
  | firstname1 | lastname1 | address1 | email1| mobile1 |
  | firstname2 | lastname2 | address2 | email2| mobile2 |