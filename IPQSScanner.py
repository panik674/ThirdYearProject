from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class IPQSScanner:
    def malicious_url_scanner(self,url):
        options = Options()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.ipqualityscore.com/threat-feeds/malicious-url-scanner")
        driver.find_element(By.ID, "url").send_keys(url)
        driver.find_element(By.ID, "url").submit()
        while driver.current_url == "https://www.ipqualityscore.com/threat-feeds/malicious-url-scanner":
            pass
        table = driver.find_element(By.XPATH, '//table[@class="email-lookup-report clearfix"][1]/tbody')
        results = []
        for i in range(0,len(table.find_elements(By.TAG_NAME, 'td'))):
            if i % 2 != 0:
                results.append(table.find_elements(By.TAG_NAME, 'td')[i].text)
        return results

    def isUnsafe(self,url):
        if self.malicious_url_scanner(url)[0] == "Clean URL - SAFE":
            return False
        else:
            return True

    def isSpamming(self,url):
        if self.malicious_url_scanner(url)[8] != "No SPAM Issues":
            return False
        else:
            return True

    def isMalware(self,url):
        if self.malicious_url_scanner(url)[4] != "No Malware Issues":
            return False
        else:
            return True

    def isPhishing(self,url):
        if self.malicious_url_scanner(url)[5] != "No Phishing Issues":
            return False
        else:
            return True

    def isSuspicious(self,url):
        if self.malicious_url_scanner(url)[1] != "Suspicious Activity":
            return False
        else:
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

        return False

    def getRiskScore(self,url):
        return self.malicious_url_scanner(url)[6].split(" ",1)[0]

