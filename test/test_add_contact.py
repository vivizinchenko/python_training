# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="firstname",
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
                                   notes="notes"))
    app.logout()