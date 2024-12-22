import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


@pytest.fixture(scope="function")
def setup():
    """Setup WebDriver for the test."""
    # Replace with the path to your WebDriver (e.g., chromedriver or geckodriver)
    opts = webdriver.ChromeOptions()  # Or `webdriver.Firefox()` for Firefox
    opts.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=opts)
    yield driver
    driver.quit()

def test_login_success(setup):
    driver = setup
    driver.get("C:\\Users\\Anu\\PycharmProjects\\selenium_training\\selenium_website_testing\\wesite\\login.html")

    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

    username_field.send_keys("testuser")
    password_field.send_keys("password123")
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)  # Allow JavaScript to execute

    assert "Login Successful" in driver.page_source, "Login failed when it should have succeeded!"

def test_login_failure(setup):
    driver = setup
    driver.get("C:\\Users\\Anu\\PycharmProjects\\selenium_training\\selenium_website_testing\\wesite\\login.html")

    username_field = driver.find_element(By.XPATH, "//input[@placeholder='Username']")
    password_field = driver.find_element(By.XPATH, "//input[@placeholder='Password']")

    username_field.send_keys("invaliduser")
    password_field.send_keys("wrongpassword")
    password_field.send_keys(Keys.RETURN)

    time.sleep(2)  # Allow JavaScript to execute

    assert "Invalid credentials!" in driver.page_source, "Login succeeded when it should have failed!"



