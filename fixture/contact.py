from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact(self):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//img[@alt='Details']").click()

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element("link text", "add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            wd.find_element("name", field_name).clear()
            wd.find_element("name", field_name).send_keys(text)

    def change_field_value_date(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element("name", field_name).click()
            Select(wd.find_element("name", field_name)).select_by_visible_text(text)
            wd.find_element("name", field_name).click()

    def filling_in_the_fields(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value_date("bday", contact.bday)
        self.change_field_value_date("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_field_value_date("aday", contact.aday)
        self.change_field_value_date("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        #дополнительные данные
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_add_contact_page()
        self.filling_in_the_fields(contact)
        # нажать кнопку создания контакта
        wd.find_element("name", "submit").click()
        self.app.open_home_page()
        self.open_contact()

    def modify(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        #выбрать первый контакт в списке
        wd.find_element("name", "selected[]").click()
        #нажать кнопку редактирования
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.filling_in_the_fields(contact)
        # нажать кнопку сохранения контакта
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        self.app.open_home_page()
        self.open_contact()

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        #выбрать первый контакт в списке
        wd.find_element("name", "selected[]").click()
        #нажать кнопку удаления
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        try:
            return len(wd.find_elements("name", "selected[]"))
        except NoSuchElementException as e:
            return 0
