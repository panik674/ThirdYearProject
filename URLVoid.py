from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class URLVoidScanner:
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    def malicious_url_scanner(self, url):

        self.driver.get("https://safeweb.norton.com/")
        self.driver.find_element(By.NAME, "url").send_keys(url)
        self.driver.find_element(By.NAME, "url").submit()

    def isUnsafe(self,url):
        self.malicious_url_scanner(url)
        while self.driver.current_url == "https://safeweb.norton.com/":
            pass
        if self.driver.find_element(By.XPATH, "//div[@class='paddingTop50 tAlignCr']/b").get_attribute("innerHTML") != "SAFE":
            return True
        return False

    def isAdult(self,url):
        adultCategories = ["Pornography", "Gore", "Violence", "Intolerance", "Extreme"]
        self.malicious_url_scanner(url)
        while self.driver.current_url == "https://safeweb.norton.com/":
            pass
        for i in self.driver.find_elements(By.XPATH, "//div[@class='span8']/ul/li"):
            for y in adultCategories:
                if y in i.get_attribute("innerHTML"):
                    return True
        return False

        return False