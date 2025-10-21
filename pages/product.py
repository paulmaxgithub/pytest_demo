from selenium.webdriver.common.by import By

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def _get_product_title(self):
        return self.driver.find_element(By.TAG_NAME, "h2").text
    
    def check_product_title(self, expected_title):
        actual_title = self._get_product_title()
        return actual_title == expected_title