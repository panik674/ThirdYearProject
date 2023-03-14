import importlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.expected_conditions
from DOMRewriter import DOMRewriter
def getScanners():
    f = open("config.txt", "r")
    scanners = f.readlines()
    for i in range(0,len(scanners)):
        scanners[i] = scanners[i].strip('\n')
    return scanners

def importScanners(scannerNum):
    module = __import__((getScanners())[scannerNum])
    scanner_class = getattr(module, getScanners()[scannerNum])
    return scanner_class()

chromeOptions = Options()

chromeOptions.add_experimental_option("detach", True)

driver_service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chromeOptions, service=driver_service)




