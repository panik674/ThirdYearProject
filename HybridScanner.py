import random
import string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class HybridScanner:


    def __init__(self,ui):
        self.options = Options()
        self.options.add_argument('--headless=new')
        self.ui = ui
    def isUnsafe(self,url):
        if self.ui.unsafeState.get() == 0:
            return False
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://www.psafe.com/dfndr-lab/")
        while driver.current_url != "https://www.psafe.com/dfndr-lab/":
            pass
        driver.find_element(By.NAME, "url").send_keys(url)
        driver.find_element(By.NAME, "url").submit()
        if driver.find_element(By.XPATH, "/html/body/div[8]/div/div/div[1]/div[2]/h1").get_attribute("innerHTML") != "THE URL YOU ENTERED IS SAFE!":
            driver.close()
            return True
        driver.close()
        return False

    def isSpamming(self, url):
        if self.ui.spamState.get() == 0:
            return False
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://sitecheck.sucuri.net/")
        while driver.current_url != "https://sitecheck.sucuri.net/":
            pass
        driver.find_element(By.ID,"websiteurl").send_keys(url)
        driver.find_element(By.ID, "websiteurl").submit()
        while driver.current_url == "https://sitecheck.sucuri.net/":
            pass
        if "No injected spam" in driver.find_element(By.XPATH, '/html/body/div[2]/section[6]/section[1]/div/div[1]/div[1]/ul/li[2]/span').text:
            driver.close()
            return False
        driver.close()
        return True

    def isMalware(self,url):
        if self.ui.malwareState.get() == 0:
            return False
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://sitecheck.sucuri.net/")
        while driver.current_url != "https://sitecheck.sucuri.net/":
            pass
        driver.find_element(By.ID, "websiteurl").send_keys(url)
        driver.find_element(By.ID, "websiteurl").submit()
        while driver.current_url == "https://sitecheck.sucuri.net/":
            pass
        if "No malware detected" in driver.find_element(By.XPATH,'/html/body/div[2]/section[6]/section[1]/div/div[1]/div[1]/ul/li[1]/span').text:
            driver.close()
            return False
        driver.close()
        return True

    def isPhishing(self,url):
        if self.ui.phishingState.get() == 0:
            return False
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://threatcop.com/phishing-url-checker")
        while driver.current_url != "https://threatcop.com/phishing-url-checker":
            pass
        driver.find_element(By.ID,"outlined-basic").send_keys(url)
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/button')
        driver.execute_script("arguments[0].click();", element)

        while True:
            try:
                if "Safe" in driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div/div/div/p[1]/span[2]').text:
                    driver.close()
                    return False
                driver.close()
                return True
            except:
                pass

    def isSuspicious(self,url):
        if self.ui.suspiciousState.get() == 0:
            return False
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://scanurl.net/")
        while driver.current_url != "https://scanurl.net/":
            pass
        driver.find_element(By.ID,"u").send_keys(url)
        driver.find_element(By.ID,"username").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(5)))
        driver.find_element(By.ID, "comment").send_keys(''.join(random.choice(string.ascii_lowercase) for i in range(30)))
        #self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/button')
        element = driver.find_element(By.XPATH,"/html/body/div/div/table/tbody/tr/td/div/div[2]/form/table/tbody/tr[7]/td[2]/input")
        driver.execute_script("arguments[0].click();", element)
        while driver.current_url == "https://scanurl.net/":
            pass
        if "None of the services we checked with report it as suspicious" in WebDriverWait(driver,100).until(EC.presence_of_element_located((By.XPATH,'/html/body/div/div/table/tbody/tr/td/table[2]/tbody/tr/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr/td[2]/span'))).text:
            driver.quit()
            return False
        driver.quit()
        return True

    def isAdult(self, url):
        if self.ui.adultState == 0:
            return False
        driver = webdriver.Chrome(options=self.options)
        adultCategories = ["Pornography", "Gore", "Violence", "Intolerance", "Extreme","Hate","Racism"]
        driver.get("https://global.sitesafety.trendmicro.com/")
        while driver.current_url != "https://global.sitesafety.trendmicro.com/":
            pass
        driver.find_element(By.NAME, "urlname").send_keys(url)
        driver.find_element(By.NAME, "urlname").submit()
        while driver.current_url == "https://global.sitesafety.trendmicro.com/":
            pass
        for i in adultCategories:
            if i in driver.find_element(By.XPATH, "/html/body/main/div/section/div/div/section[1]/div/div[6]/div[2]/div/div[2]/div").get_attribute("innerHTML"):
                driver.close()
                return True
        driver.close()
        return False

    def getRiskScore(self,url):
        driver = webdriver.Chrome(options=self.options)
        driver.get("https://zulu.zscaler.com/")
        driver.find_element(By.NAME, "url").send_keys(url)
        driver.find_element(By.NAME, "url").submit()
        while driver.current_url == "https://zulu.zscaler.com/":
            pass
        score = driver.find_element(By.XPATH,'//*[@id="rep-score"]').text
        driver.close()
        return score