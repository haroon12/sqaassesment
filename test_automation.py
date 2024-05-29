import time
from datetime import datetime

from PIL import ImageGrab
from selenium.webdriver.common.by import By

import pytest
from selenium.webdriver import Chrome
from selenium import webdriver



@pytest.fixture
def driver():
    # Initialize Chrome WebDriver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.staysucasa.com/")
    yield driver
    # Quit the WebDriver after the test
    driver.quit()


def test_verify_sucasa_standard_section(driver):
    # Task 1: Navigate to https://www.staysucasa.com/
    #driver.get("https://www.staysucasa.com/")

    sucasastandard_element = driver.find_element(By.XPATH, "//*[contains(text(), 'The Sucasa Standard')]")

    # Scroll into view to make it visible
    driver.execute_script("arguments[0].scrollIntoView();", sucasastandard_element)
    time.sleep(2)

    expected_texts = ["Work From Anywhere", "Transparent Pricing", "Premium Properties"]
    for text in expected_texts:
        assert text in driver.page_source, f"{text} not found in The Sucasa Standard section."


def test_go_to_work_from_anywhere_section(driver):
    # Navigate to https://www.staysucasa.com/
    #driver.get("https://www.staysucasa.com/")

    # Locate the element containing "Work From Anywhere" text
    work_from_anywhere_element = driver.find_element(By.XPATH, "//*[contains(text(), 'Work From Anywhere')]")

    # Scroll into view to make it visible (optional, depending on your page structure)
    driver.execute_script("arguments[0].scrollIntoView();", work_from_anywhere_element)
    time.sleep(3)


def test_verify_page_url(driver):
    # Navigate to https://www.staysucasa.com/
    #driver.get("https://www.staysucasa.com/")

    # Verify Page URL should be equal to https://www.staysucasa.com
    expected_url = "https://www.staysucasa.com/"
    assert driver.current_url.__eq__(expected_url)


def test_take_image(driver):
    # Navigate to https://www.staysucasa.com/
    #driver.get("https://www.staysucasa.com/")

    # Take a screenshot and save it with a timestamped name
    timestamp = datetime.now().strftime("%H-%M-%S")
    screenshot_name = f"FIRST_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved as {screenshot_name}")
