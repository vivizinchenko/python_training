class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element("link text", "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создать группу
        wd.find_element("name", "new").click()
        # заполнить поля группы
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)
        # нажать кнопку создания группы
        wd.find_element("name", "submit").click()
        self.open_groups_page()