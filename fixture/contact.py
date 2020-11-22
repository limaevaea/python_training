from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from model.contact import contact

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
            for element in wd.find_elements_by_name("entry"):  #for element in wd.find_element_by_xpath("//table[@id='maintable']//tr")
                cells = element.find_elements_by_tag_name("td")
                text1 = cells[1].text
                text2 = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(contact(lastname=text1, firstname=text2, id=id))
        return list(self.contact_cache)

