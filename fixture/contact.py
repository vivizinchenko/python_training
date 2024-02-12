from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact
import re
import time


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
        # дополнительные данные
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
        self.contact_cache = None

    def modify(self, contact):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.app.open_home_page()
        # выбрать первый контакт в списке
        wd.find_element("name", "selected[]").click()
        # нажать кнопку редактирования
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()
        self.filling_in_the_fields(contact)
        # нажать кнопку сохранения контакта
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        self.app.open_home_page()
        self.open_contact()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # нажать кнопку удаления
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements("name", "selected[]")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        try:
            return len(wd.find_elements("name", "selected[]"))
        except NoSuchElementException as e:
            return 0

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements("name", "entry"):
                cells = row.find_elements(By.TAG_NAME, "td")
                id = cells[0].find_element("name", "selected[]").get_attribute("value")
                firstname = cells[2].text
                lastname = cells[1].text
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, all_phones=all_phones,
                                                  all_emails=all_emails, address=address))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements("name", "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements("name", "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element("name", "firstname").get_attribute("value")
        lastname = wd.find_element("name", "lastname").get_attribute("value")
        id = wd.find_element("name", "id").get_attribute("value")
        home = wd.find_element("name", "home").get_attribute("value")
        work = wd.find_element("name", "work").get_attribute("value")
        mobile = wd.find_element("name", "mobile").get_attribute("value")
        phone2 = wd.find_element("name", "phone2").get_attribute("value")
        address = wd.find_element("name", "address").get_attribute("value")
        email = wd.find_element("name", "email").get_attribute("value")
        email2 = wd.find_element("name", "email2").get_attribute("value")
        email3 = wd.find_element("name", "email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, home=home, work=work,
                       mobile=mobile, phone2=phone2, email=email, email2=email2,
                       email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home = self.search_find("H: (.*)", text)
        work = self.search_find("W: (.*)", text)
        mobile = self.search_find("M: (.*)", text)
        phone2 = self.search_find("P: (.*)", text)
        return Contact(home=home, work=work, mobile=mobile, phone2=phone2)

    def search_find(self, regex, text):
        rs = re.search(regex, text)
        if rs:
            return rs.group(1)
        else:
            return ''

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(id)
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        alert = wd.switch_to.alert
        alert.accept()
        self.app.open_home_page()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        #self.app.open_home_page()
        wd.find_element(By.CSS_SELECTOR, "input[id='%s']" % id).click()

    def modify_contact_by_id(self, contact, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_edit_contact_by_id(id)
        self.filling_in_the_fields(contact)
        wd.find_element(By.XPATH, "//input[@value='Update']").click()
        self.contact_cache = None

    def open_edit_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element(By.XPATH, "//*[@id='%s']/../..//*[@title='Edit']" % id).click()

    def select_current_group(self, group):
        wd = self.app.wd
        self.app.open_home_page()
        select = Select(wd.find_element("name", "group"))
        select.select_by_value(group.id)

    def add_contact_to_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_id(contact.id)
        select = Select(wd.find_element(By.NAME, "to_group"))
        select.select_by_value(group.id)
        wd.find_element(By.NAME, "add").click()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_contact_from_group(self, contact, group):
        wd = self.app.wd
        #self.app.open_home_page()
        self.select_current_group(group=group)
        self.select_contact_by_id(contact.id)
        wd.execute_script("window.scrollBy(0,document.body.scrollHeight)")
        wd.find_element("name", "remove").click()
        self.app.open_home_page()
        self.contact_cache = None

def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_from_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home, contact.work, contact.mobile,
                                        contact.phone2]))))


def merge_emails_like_from_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))



