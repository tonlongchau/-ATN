from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    navigate_login_page = (
        By.CSS_SELECTOR, "#header > div.header-middle.hidden-xs.hidden-sm > div > div > div.col-lg-3.col-md-4.col-sm-5 > div > div.header-user > a:nth-child(3)")
    username = (By.ID, "customer_email")
    password = (By.ID, "customer_password")
    loginButton = (
        By.CSS_SELECTOR, "#customer_login > div.clearfix.action_account_custommer > div.action_bottom.button.dark > button")
    locked_error_text = (
        By.CSS_SELECTOR, "#customer_login > div.errors > ul > li")

    def login(self, username, password):
        self.click(self.navigate_login_page)
        self.send_keys(self.username, username)
        self.send_keys(self.password, password)
        self.click(self.loginButton)

    def get_locked_error_text(self):
        return self.get_text(self.locked_error_text)
