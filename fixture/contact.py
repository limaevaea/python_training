from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if wd.current_url.endswith("addressbook/") and len(wd.find_elements_by_xpath("(//img[@alt='Edit'])")) > 0:
            return
        wd.find_element_by_link_text("home").click()

    def init_contact_creation(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.init_contact_creation()
        self.fill_contact_form(contact)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_some_contact(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_xpath("//div[@id='content']/div").click()
        self.contact_cache = None

    def edit_some_contact(self, index, contact):
        wd = self.app.wd
        self.open_contact_page()
        self.select_contact_by_index(index)
        rows = wd.find_elements_by_name("entry")
        rows[index].find_element_by_xpath("./td[8]/a/img").click()
        # edit contact form
        self.fill_contact_form(contact)
        # submit edit contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def change_contact_date(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def change_calendar_date(self, field_date, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_xpath("(//div[@id='content']/form)").click()
            wd.find_element_by_name(field_date).click()
            wd.find_element_by_name(field_date).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_date("firstname", contact.firstname)
        self.change_contact_date("middlename", contact.middlename)
        self.change_contact_date("lastname", contact.lastname)
        self.change_contact_date("nickname", contact.nickname)
        self.change_contact_date("title", contact.title)
        self.change_contact_date("company", contact.company)
        self.change_contact_date("address", contact.address)
        self.change_contact_date("home", contact.home)
        self.change_contact_date("mobile", contact.mobile)
        self.change_contact_date("work", contact.work)
        self.change_contact_date("email", contact.email)
        self.change_calendar_date("bday", contact.birth_date)
        self.change_calendar_date("bmonth", contact.birth_month)
        self.change_calendar_date("byear", contact.birth_year)

    def submit_contact_creation(self):
        wd = self.app.wd
        self.submit_contact_creation()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                all_phones = cells[5].text #порезать строчку на части
                all_emails = cells[4].text
                self.contact_cache.append(contact(firstname=text1, lastname=text2, id=id, all_phones_from_homepage=all_phones,
                                                  all_emails_from_homepage=all_emails))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()
        #self.select_contact_by_index(index)
        #rows = wd.find_elements_by_name("entry")
        #rows[index].find_element_by_xpath("./td[8]/a/img").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        home = wd.find_element_by_name('home').get_attribute("value")
        mobile = wd.find_element_by_name('mobile').get_attribute("value")
        work = wd.find_element_by_name('work').get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")
        return contact(firstname=firstname, lastname=lastname, id=id, home=home,
                       mobile=mobile, work=work, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_to_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = re.search("H: (.*)", text).group(1)
        mobile = re.search("M: (.*)", text).group(1)
        work = re.search("W: (.*)", text).group(1)
        email = wd.find_elements_by_tag_name("a")[0]
        email2 = wd.find_elements_by_tag_name("a")[1]
        email3 = wd.find_elements_by_tag_name("a")[2]
        return contact(home=home, mobile=mobile, work=work , email=email, email2=email2, email3=email3)