from model.group import Group


def test_modify_group(app):
    #app.group.create(Group(name="gdgfdfgdfg", header="dgdgd", footer="dgdgfdg"))
    app.group.modify(Group(name="ffffffffffff", header="fffffffffff", footer="ffffffffff"))

def test_modify_group_name(app):
    app.group.modify(Group(name="New"))
