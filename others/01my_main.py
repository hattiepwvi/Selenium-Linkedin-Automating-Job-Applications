from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


EMAIL = "youjiaokuaidianhaoqilaiomalibeibeihongaowu@outlook.com"
PASSWORD = "youjiaokuaidianhaoqilaiomalibeibeihongaowu"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3741734129&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

wait = WebDriverWait(driver, 10) # 最多等待10秒钟
sign_in = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav__button-secondary")))
sign_in.click()

email = driver.find_element(By.CSS_SELECTOR, value="#username")
email.send_keys(EMAIL)
password = driver.find_element(By.CSS_SELECTOR, value="#password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)





