from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class HomePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver

    def open_website(self) -> None:
        self.driver.get("https://www.demoblaze.com/index.html")

    def find_samsung_s6(self) -> None:
        samsung_link = self.driver.find_element(By.LINK_TEXT, "Samsung galaxy s6")
        samsung_link.click()

    def go_to_monitors(self) -> None:
        monitor_link = self.driver.find_element(By.LINK_TEXT, "Monitors")
        monitor_link.click()