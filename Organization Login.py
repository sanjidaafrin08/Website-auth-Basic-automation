
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  

driver = webdriver.Chrome(options=options)
driver.maximize_window()


driver.get("https://demo/auth/login")
time.sleep(2)  


email_field = driver.find_element(By.XPATH, "(//input[@id='input-1'])[1]")
email_field.send_keys("superadmin@test.com")

password_field = driver.find_element(By.XPATH, "(//input[@id='input-3'])[1]")
password_field.send_keys("*****")


sign_in_button = driver.find_element(By.XPATH, "//button[@type='submit']")
sign_in_button.click()

time.sleep(5)  


expected_url = "https://demo/auth/login"
current_url = driver.current_url

if current_url == expected_url:
    print("Login successful! Redirected correctly.")
else:
    print("Login failed! Redirect did not happen.")


driver.quit()
