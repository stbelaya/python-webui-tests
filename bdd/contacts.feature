Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>, <email> and <mobile>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added contact


  Examples:
  | firstname   | lastname  | address            | email          | mobile      |
  | Svetlana    | Kovaleva  | Lenina 123 - 11 23 | sw@sw.ru       | 89001112233 |
  | Alexandrina | Bololo    | Moscow city        | email2@mail.qq | 99001234567 |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without the deleted contact


Scenario Outline: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname>, <address>, <email> and <mobile>
  When I edit the contact from the list according to given contact
  Then the new contact list is equal to the old list with the edited contact

    Examples:
  | firstname   | lastname    | address     | email     | mobile    |
  | nameUPD1    | lastUPD1    | address UPD1| emailUPD1 | mobileUPD1|
  | firstname2u | lastname2u  | address 2u  | email2u   | mobile2u  |
