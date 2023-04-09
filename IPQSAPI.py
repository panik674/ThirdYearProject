import json
import requests
import urllib

class IPQSAPI:
        def __init__(self,ui):
                self.key = 'uQKdGdrNZsNMB2YpmCIj9GNFsccHrtwH'
                self.ui = ui

        def malicious_url_scanner(self,url):
                url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
                x = requests.get(url)
                return (json.loads(x.text))

        def isUnsafe(self,url):
                self.results = self.malicious_url_scanner(url)
                if self.ui.unsafeState.get() == 0:
                        return False
                return self.results['unsafe']

        def isSpamming(self,url):
                if self.ui.spamState.get() == 0:
                        return False
                return self.results['spamming']

        def isMalware(self,url):
                if self.ui.malwareState.get() == 0:
                        return False
                return self.results['malware']

        def isPhishing(self,url):
                if self.ui.phishingState.get():
                        return False
                return self.results['phishing']

        def isSuspicious(self,url):
                if self.ui.suspiciousState.get() == 0:
                        return False
                return self.malicious_url_scanner(url)['suspicious']

        def isAdult(self,url):
                if self.ui.adultState.get() == 0:
                        return False
                return self.results['adult']

        def getRiskScore(self,url):
                return self.results['risk_score']





