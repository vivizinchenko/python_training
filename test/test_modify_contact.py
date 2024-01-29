# -*- coding: utf-8 -*-
from model.contact import Contact
import random


def test_modify_some_contact(app, db, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    contact = Contact(firstname="firstnamemodify",
                               middlename="middlenamemodify",
                               lastname="lastnamemodify",
                               nickname="nicknamemodify",
                               title="title modify",
                               company="company modify",
                               address="344442, j.Hrterter werwr, rerte 66",
                               home="555-555",
                               mobile="+79345554455",
                               work="555-555",
                               fax="555-555",
                               email="email0@qq.qq",
                               email2="email4@qq.qq",
                               email3="email5@qq.qq",
                               homepage="homepage",
                               bday="14",
                               bmonth="August",
                               byear="1999",
                               aday="15",
                               amonth="August",
                               ayear="2000",
                               address2="344442, j.Hrterter werwr, rerte 66b",
                               phone2="+79347444411",
                               notes="notes modify")
    old_contacts = db.get_contacts_list()
    old_contact = random.choice(old_contacts)
    app.contact.modify_contact_by_id(contact, old_contact.id)
    new_contacts = db.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

