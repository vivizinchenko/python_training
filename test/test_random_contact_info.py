from fixture.contact import merge_phones_like_from_on_home_page, merge_emails_like_from_on_home_page
from model.contact import Contact


def test_random_contact_info_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        assert sorted(contact_from_home_page[i].all_emails) == sorted(merge_emails_like_from_on_home_page(
            db_contacts[i]))
        assert sorted(contact_from_home_page[i].all_phones) == sorted(merge_phones_like_from_on_home_page(
            db_contacts[i]))
        assert contact_from_home_page[i].address == db_contacts[i].address.strip()
        assert contact_from_home_page[i].firstname == db_contacts[i].firstname.strip()
        assert contact_from_home_page[i].lastname == db_contacts[i].lastname.strip()