from fixture.contact import merge_phones_like_from_on_home_page
from model.contact import Contact


def test_phones_on_home_page(app, db):
    contact_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_contacts = sorted(db.get_contacts_list(), key=Contact.id_or_max)
    for i in range(len(contact_from_home_page)):
        assert sorted(contact_from_home_page[i].all_phones) == sorted(merge_phones_like_from_on_home_page(
            db_contacts[i]))


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home == contact_from_edit_page.home
    assert contact_from_view_page.work == contact_from_edit_page.work
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.phone2 == contact_from_edit_page.phone2
