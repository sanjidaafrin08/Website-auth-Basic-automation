from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#   go to  login page
driver = webdriver.Chrome()
driver.get("https://demo/auth/login")
driver.maximize_window()

#  Wait for Google button to be clickable and click it
try:
    google_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(text(),'Continue with Google')]"))
    )
    google_button.click()
    print(" Clicked 'Continue with Google'")
except:
    print(" Could not click the Google login button")
    driver.quit()
    exit()

#  Switch to Google login tab
time.sleep(3)
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# Step 4: Enter email
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']"))
).send_keys("xyz.com")
driver.find_element(By.XPATH, "//span[text()='Next']").click()

# Step 5: Enter password
time.sleep(3)
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "(//input[@name='Passwd'])[1]"))
).send_keys("****")
driver.find_element(By.XPATH, "//span[text()='Next']").click()

# Step 6: Wait and verify redirect
time.sleep(10)
driver.switch_to.window(windows[0])
time.sleep(5)

if driver.current_url == "https://demo/dashboard":
    print(" Successfully logged in and reached dashboard!")
else:
    print(" Login failed. Current URL:", driver.current_url)

driver.quit()
