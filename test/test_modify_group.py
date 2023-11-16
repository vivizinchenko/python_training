from model.group import Group


def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    #app.group.create(Group(name="gdgfdfgdfg", header="dgdgd", footer="dgdgfdg"))
    app.group.modify(Group(name="ffffffffffff", header="fffffffffff", footer="ffffffffff"))
    app.session.logout()

def test_modify_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="New"))
    app.session.logout()