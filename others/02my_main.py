from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

ACCOUNT_EMAIL = "youjiaokuaidianhaoqilaiomalibeibeihongaowu@outlook.com"
ACCOUNT_PASSWORD = 'youjiaokuaidianhaoqilaiomalibeibeihongaowu'

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

apply = driver.find_element(by=By.CSS_SELECTOR, value="button .artdeco-button__text")
apply.click()
submit = driver.find_element(by=By.CSS_SELECTOR, value="#ember463 .artdeco-button__text")
submit.click()