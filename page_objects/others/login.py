import time

from page_objects.common.common import Common

class Login(Common):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    email_textbox = "email"
    password_textbox = "pass"
    login_button = "login"

    def login(self, email, password):
        self.enter_text(Login.email_textbox,"id", email)
        self.enter_text(Login.password_textbox, "id", password)
        self.click(Login.login_button, "name")
        time.sleep(5)

