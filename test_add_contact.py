# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from contact import Contact
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
    
    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.open_add_contact_page(wd)
        self.create_contact(wd, Contact(firstname="firstname",
                                        middlename="middlename",
                                        lastname="lastname",
                                        nickname="nickname",
                                        title="title",
                                        company="company",
                                        address="342342, j.Hrterter werwr, rerte 66",
                                        home="444-444",
                                        mobile="+79347584455",
                                        work="444-444",
                                        fax="444-444",
                                        email="444-444",
                                        email2="444-444",
                                        email3="444-444",
                                        homepage="homepage",
                                        bday="14",
                                        bmonth="August",
                                        byear="1999",
                                        aday="15",
                                        amonth="August",
                                        ayear="2000",
                                        address2="342342, j.Hrterter werwr, rerte 66b",
                                        phone2="+79347584411",
                                        notes="notes"))
        self.open_home_page(wd)
        self.open_contact(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element("link text", "Logout").click()

    def open_contact(self, wd):
        wd.find_element(By.XPATH, "//img[@alt='Details']").click()

    def create_contact(self, wd, contact):
        # заполнить поля контакта
        wd.find_element("name", "firstname").click()
        wd.find_element("name", "firstname").clear()
        wd.find_element("name", "firstname").send_keys(contact.firstname)
        wd.find_element("name", "middlename").click()
        wd.find_element("name", "middlename").clear()
        wd.find_element("name", "middlename").send_keys(contact.middlename)
        wd.find_element("name", "lastname").click()
        wd.find_element("name", "lastname").clear()
        wd.find_element("name", "lastname").send_keys(contact.lastname)
        wd.find_element("name", "nickname").click()
        wd.find_element("name", "nickname").clear()
        wd.find_element("name", "nickname").send_keys(contact.nickname)
        wd.find_element("name", "title").click()
        wd.find_element("name", "title").clear()
        wd.find_element("name", "title").send_keys(contact.title)
        wd.find_element("name", "company").click()
        wd.find_element("name", "company").clear()
        wd.find_element("name", "company").send_keys(contact.company)
        wd.find_element("name", "address").click()
        wd.find_element("name", "address").clear()
        wd.find_element("name", "address").send_keys(contact.address)
        wd.find_element("name", "home").click()
        wd.find_element("name", "home").clear()
        wd.find_element("name", "home").send_keys(contact.home)
        wd.find_element("name", "mobile").click()
        wd.find_element("name", "mobile").clear()
        wd.find_element("name", "mobile").send_keys(contact.mobile)
        wd.find_element("name", "work").click()
        wd.find_element("name", "work").clear()
        wd.find_element("name", "work").send_keys(contact.work)
        wd.find_element("name", "fax").click()
        wd.find_element("name", "fax").clear()
        wd.find_element("name", "fax").send_keys(contact.fax)
        wd.find_element("name", "email").click()
        wd.find_element("name", "email").clear()
        wd.find_element("name", "email").send_keys(contact.email)
        wd.find_element("name", "email2").click()
        wd.find_element("name", "email2").clear()
        wd.find_element("name", "email2").send_keys(contact.email2)
        wd.find_element("name", "email3").click()
        wd.find_element("name", "email3").clear()
        wd.find_element("name", "email3").send_keys(contact.email3)
        wd.find_element("name", "homepage").click()
        wd.find_element("name", "homepage").clear()
        wd.find_element("name", "homepage").send_keys(contact.homepage)
        wd.find_element("name", "bday").click()
        Select(wd.find_element("name", "bday")).select_by_visible_text(contact.bday)
        wd.find_element("name", "bday").click()
        wd.find_element("name", "bmonth").click()
        Select(wd.find_element("name", "bmonth")).select_by_visible_text(contact.bmonth)
        wd.find_element("name", "bmonth").click()
        wd.find_element("name", "byear").click()
        wd.find_element("name", "byear").clear()
        wd.find_element("name", "byear").send_keys(contact.byear)
        wd.find_element("name", "aday").click()
        Select(wd.find_element("name", "aday")).select_by_visible_text(contact.aday)
        wd.find_element("name", "aday").click()
        wd.find_element("name", "amonth").click()
        Select(wd.find_element("name", "amonth")).select_by_visible_text(contact.amonth)
        wd.find_element("name", "amonth").click()
        wd.find_element("name", "ayear").click()
        wd.find_element("name", "ayear").clear()
        wd.find_element("name", "ayear").send_keys(contact.ayear)
        #дополнительные данные
        wd.find_element("name", "address2").click()
        wd.find_element("name", "address2").clear()
        wd.find_element("name", "address2").send_keys(contact.address2)
        wd.find_element("name", "phone2").click()
        wd.find_element("name", "phone2").clear()
        wd.find_element("name", "phone2").send_keys(contact.phone2)
        wd.find_element("name", "notes").click()
        wd.find_element("name", "notes").clear()
        wd.find_element("name", "notes").send_keys(contact.notes)
        # нажать кнопку создания контакта
        wd.find_element("name", "submit").click()

    def open_add_contact_page(self, wd):
        wd.find_element("link text", "add new").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def login(self, wd, username, password):
        wd.find_element("name", "user").click()
        wd.find_element("name", "user").clear()
        wd.find_element("name", "user").send_keys(username)
        wd.find_element("name", "pass").click()
        wd.find_element("name", "pass").clear()
        wd.find_element("name", "pass").send_keys(password)
        wd.find_element("css selector", "input[type='submit']").click()
    
    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
