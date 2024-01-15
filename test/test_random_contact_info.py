from random import randrange
from fixture.contact import merge_phones_like_from_on_home_page, merge_emails_like_from_on_home_page


def test_random_contact_info_on_home_page(app):
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert sorted(contact_from_home_page.all_emails) == sorted(merge_emails_like_from_on_home_page(
        contact_from_edit_page))
    assert sorted(contact_from_home_page.all_phones) == sorted(merge_phones_like_from_on_home_page(
        contact_from_edit_page))
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname