import random

from model.contact import Contact
from test.test_add_contacts_in_group import test_add_contact_in_group


def test_delete_contact_from_group(app, db, db_orm, check_ui):
    if len(db.get_contacts_list()) == 0 or len(db.get_groups_with_contacts()) == 0:
        test_add_contact_in_group(app=app, db=db, db_orm=db_orm, check_ui=check_ui)
    group = random.choice(db.get_groups_with_contacts())
    old_contacts_in_group = db_orm.get_contacts_in_group(group=group)
    contact = random.choice(old_contacts_in_group)
    old_contacts_not_in_group = db_orm.get_contacts_not_in_group(group=group)
    app.contact.delete_contact_from_group(contact=contact, group=group)
    new_contacts_in_group = db_orm.get_contacts_in_group(group=group)
    new_contacts_not_in_group = db_orm.get_contacts_not_in_group(group=group)
    assert len(old_contacts_in_group) - 1 == len(new_contacts_in_group)
    assert len(old_contacts_not_in_group) + 1 == len(new_contacts_not_in_group)
    old_contacts_in_group.remove(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)