from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions
from IPQSAPI import IPQS

chromeOptions = Options()

chromeOptions.add_experimental_option("detach", True)

driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chromeOptions, service=driver_service)
#webbrowser.open("https://www.youtube.com/")
driver.get("https://www.google.co.uk/")
ipqs = IPQS()
print(ipqs.isAdult("https://www.pornhub.com/"))

while True:

    driver.switch_to.window(driver.window_handles[len(driver.window_handles) - 1])
    links = driver.find_elements(By.XPATH, "//a[@href]")
    for link in links:
        driver.execute_script("arguments[0].removeAttribute('href')", link)


