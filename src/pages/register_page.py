from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage
from src.utility import xlReader


class RegisterPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    navigatr_register_page = (
        By.CSS_SELECTOR, "#header > div.header-middle.hidden-xs.hidden-sm > div > div > div.col-lg-3.col-md-4.col-sm-5 > div > div.header-user > a:nth-child(5)")
    lastname = (By.XPATH, '//input[@id="last_name"]')
    firstname = (By.XPATH, '//input[@id="first_name"]')
    birthday = (By.XPATH, '//input[@id="birthday"]')
    email = (By.XPATH, '//input[@name="customer[email]"]')
    password = (By.XPATH, '//input[@id="password"]')
    registerButton = (By.XPATH, "//*[@id='create_customer']/div[7]/div/input")
    verify_account = (By.XPATH, '//*[@id="customer_sidebar"]/div[1]/div[1]')
    error_text = (By.XPATH, '//*[@id="create_customer"]/div[1]')

    def register(self, lastname, firstname, gender, birthday, email, password):
        self.click(self.navigatr_register_page)
        self.send_keys(self.lastname, lastname)
        self.send_keys(self.firstname, firstname)
        self.driver.find_element(By.ID, gender).click()
        self.send_keys(self.birthday, birthday)
        self.send_keys(self.email, email)
        self.send_keys(self.password, password)
        self.click(self.registerButton)

        """ self.click(self.loginButton) """

    def verifyRegister(self):
        return self.get_text(self.verify_account)

    def get_error_text(self):
        return self.get_text(self.error_text)
