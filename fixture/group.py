from selenium.common.exceptions import NoSuchElementException
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements("name", "new")) > 0):
            wd.find_element("link text", "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # создать группу
        wd.find_element("name", "new").click()
        self.filling_in_the_fields(group)
        wd.find_element("name", "submit").click()
        self.open_groups_page()
        self.group_cache = None

    def filling_in_the_fields(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.header)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #нажать кнопку удаления
        wd.find_element("name", "delete").click()
        self.open_groups_page()
        self.group_cache = None

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element("name", "selected[]").click()

    def modify(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        #нажать кнопку редактирования
        wd.find_element("name", "edit").click()
        self.filling_in_the_fields(group)
        wd.find_element("name", "update").click()
        self.open_groups_page()
        self.group_cache = None

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        try:
            return len(wd.find_elements("name", "selected[]"))
        except NoSuchElementException as e:
            return 0

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.group_cache = []
            for element in wd.find_elements("css selector", "span.group"):
                text = element.text
                id = element.find_element("name", "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, id=id))
        return list(self.group_cache)
