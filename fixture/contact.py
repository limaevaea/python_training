from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_id("header").click()

    def init_contact_creation(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_link_text("add new").click()

    def create_new_contact(self, contact):
        wd = self.app.wd
        self.init_contact_creation()
        self.fill_contact_form(contact)
        wd.find_element_by_name("theform").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])").click()
        # edit contact form
        self.fill_contact_form(contact)
        # submit edit contact
        wd.find_element_by_name("update").click()

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