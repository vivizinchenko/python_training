import random
from faker import Faker
import string
import pytest
from model.contact import Contact
import  time

fake = Faker()

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [
    Contact(firstname=firstname,
            middlename=middlename,
            lastname=lastname,
            nickname=nickname,
            title=title,
            company=company,
            address=address,
            home=str(number)+"-"+str(number),
            mobile="+7"+str(mobile),
            work=str(number)+"-"+str(number),
            fax=str(number)+"-"+str(number),
            email=fake.email(),
            email2=fake.email(),
            email3=fake.email(),
            homepage=homepage,
            bday=str(bday),
            bmonth=month,
            byear=byear,
            aday=str(aday),
            amonth=month,
            ayear=ayear,
            address2=address2,
            phone2="+7"+str(mobile),
            notes=notes)
    for firstname in [random_string("firstname", 10)]
    for middlename in [random_string("middlename", 10)]
    for lastname in [random_string("lastname", 10)]
    for nickname in [random_string("nickname", 10)]
    for title in ["", random_string("title", 30)]
    for company in ["", random_string("company", 10)]
    for address in [fake.address()]
    for address2 in ["", fake.address()]
    for number in [random.randint(1, 999)]
    for mobile in [random.randint(1000000000, 9999999999)]
    for email in [random_string("email", 10)]
    for homepage in [random_string("homepage", 10)]
    for bday in [random.randint(1, 31)]
    for month in [fake.month_name()]
    for byear in [random.randint(1990, 2020)]
    for aday in [random.randint(1, 31)]
    for ayear in [random.randint(1990, 2020)]
    for notes in [random_string("notes", 10)]
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    time.sleep(1)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
