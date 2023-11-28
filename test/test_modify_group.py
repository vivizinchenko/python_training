from model.group import Group


def test_modify_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify(Group(name="ffffffffffff", header="fffffffffff", footer="ffffffffff"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

def test_modify_group_name(app):
    old_groups = app.group.get_group_list()
    app.group.modify(Group(name="New"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)