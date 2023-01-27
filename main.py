from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()

chromeOptions.add_experimental_option("detach", True)

driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chromeOptions, service=driver_service)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

links = driver.find_elements(By.XPATH,"//a[@href]")

for i in links:
    driver.execute_script("arguments[0].removeAttribute('href')", i)
