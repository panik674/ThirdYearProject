from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class DOMRewriter:
    def disableLinks(self,driver):
        while True:
            links = driver.find_elements(By.XPATH, "//a[@href]")
            for link in links:
                try:
                    driver.execute_script("arguments[0].setAttribute('href','#_')", link)
                    driver.execute_script("arguments[0].setAttribute('title','Risk Score: *placeholder*')", link)
                except:
                    pass