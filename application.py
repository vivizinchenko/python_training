from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("css selector", "input[type='submit']").click()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element("link text", "groups").click()

    def create_group(self, group):
        wd = self.wd
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

    def logout(self):
        wd = self.wd
        wd.find_element("link text", "Logout").click()

    def destroy(self):
        self.wd.quit()
