from selenium.webdriver.common.by import By

from src.pages.base_page import BasePage

class SearchPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        
    search_input = (By.NAME, "q")
    search_submit = (By.XPATH, "//*[@id='searchsubmit']")
    search_result = (By.XPATH, '//*[@id="search"]/div[1]/div/div[1]/div/div[2]/div[1]/h3')
    error_text = (By.XPATH, '//*[@id="search"]/div/h2')
    
    def search(self, searhname):
        self.send_keys(self.search_input, searhname)
        self.click(self.search_submit)
        
    def product_result(self):
        return self.get_text(self.search_result)
    
    def get_error(self):
        return self.get_text(self.error_text)
        
        