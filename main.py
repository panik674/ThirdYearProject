from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from DOMRewriter import DOMRewriter
from Interface import interface
def getScanners():
    f = open("config.txt", "r")
    scanners = f.readlines()
    for i in range(0, len(scanners)):
        scanners[i] = scanners[i].strip('\n')
    return scanners
def startBrowser():
    chromeOptions = Options()
    chromeOptions.add_experimental_option("detach", True)
    driver_service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(options=chromeOptions, service=driver_service)
    ui = interface(getScanners())
    dw = DOMRewriter(driver,getScanners(),ui)
    dw.disableLinks()

startBrowser()



