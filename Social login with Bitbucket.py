from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Launch browser and go to login page
driver = webdriver.Chrome()
driver.get("https://demo/auth/login")
driver.maximize_window()

# Step 1: Click "Continue with Bitbucket"
try:
    bitbucket_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//div[contains(text(),'Continue with Bitbucket')])[1]"))
    )
    bitbucket_btn.click()
    print("Clicked 'Continue with Bitbucket'")
except Exception as e:
    print("Failed to click Bitbucket button:", e)
    driver.quit()
    exit()

# Step 2: Enter email in Bitbucket
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='username']"))
    )
    email_field.send_keys("xyz.com")
    continue_btn = driver.find_element(By.XPATH, "//span[normalize-space()='Continue']")
    continue_btn.click()
    print("Entered Bitbucket email and clicked Continue")
except Exception as e:
    print("Error entering Bitbucket email:", e)
    driver.quit()
    exit()

# Step 3: Click "Continue with Google" on Bitbucket page
try:
    google_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[@class='css-178ag6o']"))
    )
    google_btn.click()
    print("Clicked 'Continue with Google'")
except Exception as e:
    print("Failed to click 'Continue with Google':", e)
    driver.quit()
    exit()

# Step 4: Switch to Google login tab
time.sleep(3)
windows = driver.window_handles
driver.switch_to.window(windows[-1])

# Step 5: Enter Google email
try:
    email_input = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']"))
    )
    email_input.send_keys("xyz")
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    print("Entered Google email")
except Exception as e:
    print("Error entering Google email:", e)
    driver.quit()
    exit()

# Step 6: Enter Google password (updated)
try:
    # Wait for password field to be present in DOM
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "Passwd"))
    )

    # Wait until it's visible and clickable
    password_input = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.NAME, "Passwd"))
    )

    # Scroll into view (sometimes helps)
    driver.execute_script("arguments[0].scrollIntoView(true);", password_input)
    time.sleep(1)

    # Send password
    password_input.send_keys("****")
    driver.find_element(By.XPATH, "//span[text()='Next']").click()
    print(" Entered Google password")
except Exception as e:
    print(" Error entering Google password:", e)
    driver.quit()
    exit()
# Step 7: Wait for redirection and verify dashboard page
try:
    # Wait for the URL to change to the dashboard
    WebDriverWait(driver, 20).until(
        EC.url_to_be("https://demo/dashboard")
    )
    
    current_url = driver.current_url
    if current_url == "https://demo/dashboard":
        print(" Login successful! Reached dashboard.")
    else:
        print(f" Login possibly failed. Current URL: {current_url}")
except Exception as e:
    print(" Error verifying dashboard login:", e)
