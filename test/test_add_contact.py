# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname",
                               middlename="middlename",
                               lastname="lastname",
                               nickname="nickname",
                               title="title",
                               company="company",
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
                               notes="notes")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
