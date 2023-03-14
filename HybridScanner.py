import random
import string
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class HybridScanner:
    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    def isUnsafe(self,url):
        self.driver.get("https://safeweb.norton.com/")
        self.driver.find_element(By.NAME, "url").send_keys(url)
        self.driver.find_element(By.NAME, "url").submit()
        while self.driver.current_url == "https://safeweb.norton.com/":
            pass
        if self.driver.find_element(By.XPATH, "//div[@class='paddingTop50 tAlignCr']/b").get_attribute("innerHTML") != "SAFE":
            return True
        return False

    def isSpamming(self, url):
        self.driver.get("https://sitecheck.sucuri.net/")
        self.driver.find_element(By.ID,"websiteurl").send_keys(url)
        self.driver.find_element(By.ID, "websiteurl").submit()
        while self.driver.current_url == "https://sitecheck.sucuri.net/":
            pass
        if "No injected spam" in self.driver.find_element(By.XPATH, '//*[@id="results"]/section[1]/div/div[1]/div[1]/ul/li[2]/span').text:
            return False
        return True

    def isMalware(self,url):
        self.driver.get("https://sitecheck.sucuri.net/")
        self.driver.find_element(By.ID, "websiteurl").send_keys(url)
        self.driver.find_element(By.ID, "websiteurl").submit()
        while self.driver.current_url == "https://sitecheck.sucuri.net/":
            pass
        if "No malware detected" in self.driver.find_element(By.XPATH,'//*[@id="results"]/section[1]/div/div[1]/div[1]/ul/li[1]/span').text:
            return False
        return True

    def isPhishing(self,url):
        self.driver.get("https://threatcop.com/phishing-url-checker")
        self.driver.find_element(By.ID,"outlined-basic").send_keys(url)
        self.driver.find_element(By.XPATH, '//*[@id="__next"]/div/div[2]/div/div[3]/button').click()
        while True:
            try:
                if "Safe" in self.driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[3]/div/div/div/p[1]/span[2]').text:
                    return False
                return True
            except:
                pass

    def isSuspicious(self,url):
        self.driver.get("https://scanurl.net/")
        self.driver.find_element(By.ID,"u").send_keys(url)
        self.driver.find_element(By.ID,"username").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        self.driver.find_element(By.ID, "comment").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(30)))
        self.driver.find_element(By.ID,"uesb").click()
        while self.driver.current_url == "https://scanurl.net/":
            pass
        if "None of the services we checked with report it as suspicious" in self.driver.find_element(By.XPATH,'/html/body/div/div/table/tbody/tr/td/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/span').text:
            return False
        return True


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

    def getRiskScore(self,url):
        self.driver.get("https://zulu.zscaler.com/")
        self.driver.find_element(By.NAME, "url").send_keys(url)
        self.driver.find_element(By.NAME, "url").submit()
        while self.driver.current_url == "https://zulu.zscaler.com/":
            pass
        return int(self.driver.find_element(By.XPATH,'//*[@id="rep-score"]').text)