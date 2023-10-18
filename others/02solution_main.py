from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "youjiaokuaidianhaoqilaiomalibeibeihongaowu@outlook.com"
ACCOUNT_PASSWORD = 'youjiaokuaidianhaoqilaiomalibeibeihongaowu'
PHONE = 'youjiaokuaidianhaoqilaiomalibeibeihongaowu'

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get(
    "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491"
    "&keywords=python%20developer"
    "&location=London%2C%20England%2C%20United%20Kingdom"
    "&redirect=false&position=1&pageNum=0"
)

# Click Reject Cookies Button
# time.sleep(10)
# reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
# reject_button.click()

# Click Sign in Button
time.sleep(10)
sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value=".nav__button-secondary")
sign_in_button.click()

# Sign in
time.sleep(5)
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)
password_field.send_keys(Keys.ENTER)

# You may be presented with a CAPTCHA - Solve the Puzzle Manually
input("Press Enter when you have solved the Captcha")

#Locate the apply button
time.sleep(5)
apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
apply_button.click()

#If application requires phone number and the field is empty, then fill in the number.
time.sleep(5)
phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
if phone.text == "":
    phone.send_keys(PHONE)

#Submit the application
time.sleep(5)
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
submit_button.click()
