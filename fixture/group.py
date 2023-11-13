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
        self.filling_in_the_fields(group)
        wd.find_element("name", "submit").click()
        self.open_groups_page()

    def filling_in_the_fields(self, group):
        wd = self.app.wd
        wd.find_element("name", "group_name").click()
        wd.find_element("name", "group_name").clear()
        wd.find_element("name", "group_name").send_keys(group.name)
        wd.find_element("name", "group_header").click()
        wd.find_element("name", "group_header").clear()
        wd.find_element("name", "group_header").send_keys(group.header)
        wd.find_element("name", "group_footer").click()
        wd.find_element("name", "group_footer").clear()
        wd.find_element("name", "group_footer").send_keys(group.footer)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        #выбрать первую группу в списке
        wd.find_element("name", "selected[]").click()
        #нажать кнопку удаления
        wd.find_element("name", "delete").click()
        self.open_groups_page()

    def modify(self, group):
        wd = self.app.wd
        self.open_groups_page()
        #выбрать первую группу в списке
        wd.find_element("name", "selected[]").click()
        #нажать кнопку редактирования
        wd.find_element("name", "edit").click()
        self.filling_in_the_fields(group)
        wd.find_element("name", "update").click()
        self.open_groups_page()
