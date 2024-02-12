import random
from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app, db, db_orm, check_ui):
    if len(db.get_contacts_list()) == 0:
        app.contact.create(Contact(firstname="contact"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="group"))
    groups = db.get_group_list()
    group = random.choice(groups)
    if len(db_orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create(Contact(firstname="contact"))
    old_contacts_not_in_groups = db_orm.get_contacts_not_in_group(group)
    contact = random.choice(old_contacts_not_in_groups)
    old_contacts_in_group = db_orm.get_contacts_in_group(group=group)
    app.contact.add_contact_to_group(contact=contact, group=group)
    new_contacts_not_in_groups = db_orm.get_contacts_not_in_group(group)
    new_contacts_in_group = db_orm.get_contacts_in_group(group=group)
    assert len(old_contacts_not_in_groups) - 1 == len(new_contacts_not_in_groups)
    assert len(old_contacts_in_group) + 1 == len(new_contacts_in_group)
    old_contacts_in_group.append(contact)
    assert sorted(old_contacts_in_group, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)