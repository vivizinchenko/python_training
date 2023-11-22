from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify(Group(name="ffffffffffff", header="fffffffffff", footer="ffffffffff"))

def test_modify_group_name(app):
    app.group.modify(Group(name="New"))
