
class SessionHelperContact:

    def __init__(self, cont_app):
        self.cont_app = cont_app


    def login(self, username, password):
        wd = self.cont_app.wd
        self.cont_app.open_homepage()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_id("LoginForm").submit()

    def logout(self):
        wd = self.cont_app.wd
        wd.find_element_by_link_text("Logout").click()