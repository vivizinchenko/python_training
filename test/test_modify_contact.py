# -*- coding: utf-8 -*-
from model.contact import Contact


def test_modify_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.modify(Contact(firstname="firstnamemodify",
                               middlename="middlenamemodify",
                               lastname="lastnamemodify",
                               nickname="nicknamemodify",
                               title="title modify",
                               company="company modify",
                               address="342342, j.Hrterter werwr, rerte 66",
                               home="444-444",
                               mobile="+79347584455",
                               work="444-444",
                               fax="444-444",
                               email="444-444",
                               email2="444-444",
                               email3="444-444",
                               homepage="homepage",
                               bday="14",
                               bmonth="August",
                               byear="1999",
                               aday="15",
                               amonth="August",
                               ayear="2000",
                               address2="342342, j.Hrterter werwr, rerte 66b",
                               phone2="+79347584411",
                               notes="notes modify"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_modify_contact_firstname(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.modify(Contact(firstname="newfirstnamemodify"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
