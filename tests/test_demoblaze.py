from time import sleep
from selenium.webdriver.common.by import By
import pytest
from pages.homepage import HomePage
from pages.product import ProductPage

@pytest.fixture(autouse=True)
def home_page_setup(driver):
    homepage = HomePage(driver)
    homepage.open_website()
    return homepage

def test_open_SamsungS6(driver, home_page_setup):
    home_page_setup.find_samsung_s6()
    product_page = ProductPage(driver)
    assert product_page.check_product_title("Samsung galaxy s6")

def test_find_two_monitors(driver, home_page_setup):
    home_page_setup.go_to_monitors()

    sleep(3)
    
    monitor_links = driver.find_elements(By.CSS_SELECTOR, "div.card.h-100 > a[href]")
    assert len(monitor_links) == 2, "Expected exactly 2 monitors to be displayed"