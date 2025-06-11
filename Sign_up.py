from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os

# Setup
driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://example.com/signup")  # Replace with actual URL
    driver.find_element(By.ID, "name").send_keys("Test User")
    driver.find_element(By.ID, "email").send_keys("test@example.com")
    driver.find_element(By.ID, "password").send_keys("Test1234!")
    driver.find_element(By.ID, "signupBtn").click()
    
    # Assertion or check
    assert "Welcome" in driver.title  # Replace with actual check
    print("Signup test passed.")

except Exception as e:
    print("Signup test failed:", e)
    if not os.path.exists("screenshots"):
        os.makedirs("screenshots")
    driver.save_screenshot("screenshots/signup_failure.png")

finally:
    driver.quit()
