import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# === Configuration ===
NAUKRI_USERNAME = os.environ.get("NAUKRI_USERNAME")
NAUKRI_PASSWORD = os.environ.get("NAUKRI_PASSWORD")
RESUME_PATH = 'C:/Users/india/Desktop/Devops/Resume/NAGA_PARAMESWARA_REDDY.pdf'

# === Headless Chrome Options ===
chrome_options = Options()
chrome_options.add_argument("--headless")        # run without UI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# === ChromeDriver path ===
service = Service(r"C:\Users\india\Downloads\chromedriver-win32\chromedriver.exe")

# === Start Browser ===
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 20)

try:
    # 1. Go to login page
    driver.get("https://www.naukri.com/nlogin/login")

    # 2. Login
    wait.until(EC.presence_of_element_located((By.ID, "usernameField"))).send_keys(NAUKRI_USERNAME)
    driver.find_element(By.ID, "passwordField").send_keys(NAUKRI_PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Login']").click()

    # 3. Wait for login to complete
    wait.until(EC.url_contains("naukri.com"))

    # 4. Go to profile
    driver.get("https://www.naukri.com/mnjuser/profile")

    # 5. Wait and upload resume
    upload_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))

    # Send resume file path
    upload_input.send_keys(RESUME_PATH)

    # 6. Wait a few seconds to ensure upload completes
    time.sleep(10)

    print("✅ Resume updated successfully on Naukri.")

finally:
    driver.quit()
