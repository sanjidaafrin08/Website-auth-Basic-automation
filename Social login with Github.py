from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Go to  login page
driver = webdriver.Chrome()
driver.get("https://demo/auth/login")
driver.maximize_window()

# Step 2: Click on "Continue with Github"
try:
    github_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//button[@type='button'])[3]"))
    )
    github_button.click()
    print(" Clicked 'Continue with GitHub'")
except:
    print(" Could not click the GitHub login button")
    driver.quit()
    exit()

# Step 3: Switch to GitHub login tab
time.sleep(3)
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# Step 4: Enter GitHub username/email
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "login_field"))
).send_keys("xyz.com")

# Step 5: Enter password
driver.find_element(By.ID, "password").send_keys("****")

# Step 6: Click Sign in
driver.find_element(By.NAME, "commit").click()

# Step 7: Switch back to main window and verify URL
time.sleep(5)
driver.switch_to.window(windows[0])
time.sleep(5)

if "dashboard" in driver.current_url:
    print(" Successfully logged in and reached dashboard!")
else:
    print(" Login failed. Current URL:", driver.current_url)

driver.quit()
