from tkinter import *
from selenium.webdriver.common.by import By


class DOMRewriter:
    def __init__(self,driver,scanners,ui):
        self.driver = driver
        self.scanners = scanners
        self.ui = ui
        self.blackList = []
        self.whiteblackRead("BlackList.txt",self.blackList)
        self.whiteList = []
        self.whiteblackRead("WhiteList.txt",self.whiteList)



    def importScanners(self,scannerNum):
        module = __import__(self.scanners[scannerNum])
        scanner_class = getattr(module, self.scanners[scannerNum])
        return scanner_class(self.ui)
    def disableLinks(self):
        self.ui.refresh = Button(self.ui.root, text="Refresh", command=self.disable).pack()
        whiteblacklistValue = StringVar()
        self.ui.whiteblackList = Entry(self.ui.root,textvariable=whiteblacklistValue).pack()
        self.ui.blackList = Button(self.ui.root,text="Black List",command=lambda: self.whiteblackList(whiteblacklistValue.get(),"BlackList.txt") ).pack(side=LEFT)
        self.ui.whiteList = Button(self.ui.root,text="White List",command=lambda: self.whiteblackList(whiteblacklistValue.get(),"WhiteList.txt")).pack(side=RIGHT)

        currentUrl = self.driver.current_url
        while True:
            try:
                self.ui.root.update()
                if currentUrl != self.driver.current_url:
                    self.disable()
                    currentUrl = self.driver.current_url
            except:
                quit()

    def disable(self):
        if self.ui.option.get() == "Scanner":
            self.scanner = self.importScanners(0)
        else:
            self.scanner = self.importScanners(self.ui.options.index(self.ui.option.get()))
        cache = {}

        links = self.driver.find_elements(By.XPATH, "//a[@href]")
        for link in links:

            linkName = link.get_attribute("href")

            if linkName in cache:
                riskStatus = cache[linkName]["RiskScore"]
                if cache[linkName]["SecurityTests"] and int(riskStatus) < self.ui.riskScoreState.get():
                    self.driver.execute_script("arguments[0].setAttribute('onclick','return true;')", link)
                else:
                    self.driver.execute_script("arguments[0].setAttribute('onclick','return false;')", link)

            elif linkName in self.blackList:
                riskStatus = "BlackListed"
                self.driver.execute_script("arguments[0].setAttribute('onclick','return false;')", link)
            elif linkName in self.whiteList:
                riskStatus = "WhiteListed"
                self.driver.execute_script("arguments[0].setAttribute('onclick','return true;')", link)

            else:
                securityTests = self.securityTests(linkName)
                riskStatus = str(self.scanner.getRiskScore(linkName))
                cache[linkName] = {"SecurityTests": securityTests, "RiskScore": riskStatus}
                if securityTests and int(riskStatus) < self.ui.riskScoreState.get():
                    self.driver.execute_script("arguments[0].setAttribute('onclick','return true;')", link)
                else:
                    self.driver.execute_script("arguments[0].setAttribute('onclick','return false;')", link)
            self.driver.execute_script("arguments[0].setAttribute('title','Risk Score: " + riskStatus + "')",link)
    def securityTests(self,url):
        if self.scanner.isUnsafe(url):
            return False
        if self.scanner.isSpamming(url):
            return False
        if self.scanner.isMalware(url):
            return False
        if self.scanner.isPhishing(url):
            return False
        if self.scanner.isSuspicious(url):
            return False
        if self.scanner.isAdult(url):
            return False
        return True


    def whiteblackRead(self,file,list):
        f = open(file)
        lines = f.readlines()
        for i in range(0, len(lines)):
            list.append(lines[i].strip("\n"))
    def whiteblackWrite(self,url,file):
        fr = open(file,"r")
        lines = fr.readlines()
        for i in range(0,len(lines)):
            if url == lines[i].strip("\n"):
                return False
        fa = open(file, "a")
        fa.write(url+"\n")

