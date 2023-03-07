from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions
from IPQSAPI import IPQSAPI
from IPQSScraper import IPQScraper
from URLVoid import URLVoidScanner
from DOMRewriter import DOMRewriter

chromeOptions = Options()

chromeOptions.add_experimental_option("detach", True)

driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chromeOptions, service=driver_service)
driver.get("https://www.google.co.uk/")




