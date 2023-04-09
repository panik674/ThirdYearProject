from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

class IPQSScanner:
    options = Options()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    ui = None
    results = None

    def __init__(self,ui):
        self.ui = ui
    def malicious_url_scanner(self,url):

        self.driver.get("https://www.ipqualityscore.com/threat-feeds/malicious-url-scanner")
        self.driver.find_element(By.ID, "url").send_keys(url)
        self.driver.find_element(By.ID, "url").submit()
        while self.driver.current_url == "https://www.ipqualityscore.com/threat-feeds/malicious-url-scanner":
            pass
        table = self.driver.find_element(By.XPATH, '//table[@class="email-lookup-report clearfix"][1]/tbody')
        results = []
        for i in range(0,len(table.find_elements(By.TAG_NAME, 'td'))):
            if i % 2 != 0:
                results.append(table.find_elements(By.TAG_NAME, 'td')[i].text)
        return results

    def isUnsafe(self,url):
        self.results = self.malicious_url_scanner(url)
        if self.ui.unsafeState.get() == 0:
            return False
        elif self.results[0] == "Clean URL - SAFE":
            return False
        else:
            return True

    def isSpamming(self,url):
        if self.ui.spamState.get() == 0:
            return False
        elif self.results[8] == "No SPAM Issues":
            return False
        else:
            return True

    def isMalware(self,url):
        if self.ui.malwareState.get() == 0:
            return False
        elif self.results[4] == "No Malware Issues":
            return False
        else:
            return True

    def isPhishing(self,url):
        if self.ui.phishingState.get() == 0:
            return False
        elif self.results[5] == "No Phishing Issues":
            return False
        else:
            return True

    def isSuspicious(self,url):
        if self.ui.suspiciousState.get() == 0:
            return False
        elif self.results[1] != "Suspicious Activity":
            return False
        else:
            return True

    def isAdult(self, url):
        if self.ui.adultState.get() == 0:
            return False
        adultCategories = ["Pornography", "Gore", "Violence", "Intolerance", "Extreme", "Hate", "Racism"]
        self.driver.get("https://global.sitesafety.trendmicro.com/")
        while self.driver.current_url != "https://global.sitesafety.trendmicro.com/":
            pass
        self.driver.find_element(By.NAME, "urlname").send_keys(url)
        self.driver.find_element(By.NAME, "urlname").submit()
        while self.driver.current_url == "https://global.sitesafety.trendmicro.com/":
            pass
        for i in adultCategories:
            if i in self.driver.find_element(By.XPATH,"/html/body/main/div/section/div/div/section[1]/div/div[6]/div[2]/div/div[2]/div").get_attribute("innerHTML"):
                return True
        return False


    def getRiskScore(self,url):
        return self.results[6].split(" ",1)[0]

#scanner = IPQSScanner()
#print(scanner.isSpamming("https://www.w3schools.com/"))
