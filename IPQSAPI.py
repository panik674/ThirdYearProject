import json
import requests
import urllib

class IPQSAPI:
        key = 'fi4mcakq7erKrWA3aW4CmGIxqcOuWkSk'

        def malicious_url_scanner(self,url):
                url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
                x = requests.get(url)
                return (json.loads(x.text))

        def isUnsafe(self,url):
                return self.malicious_url_scanner(url)['unsafe']

        def isSpamming(self,url):
                return self.malicious_url_scanner(url)['spamming']

        def isMalware(self,url):
                return self.malicious_url_scanner(url)['malware']

        def isPhishing(self,url):
                return self.malicious_url_scanner(url)['phishing']

        def isSuspicious(self,url):
                return self.malicious_url_scanner(url)['suspicious']

        def isAdult(self,url):
                return self.malicious_url_scanner(url)['adult']

        def getRiskScore(self,url):
                return self.malicious_url_scanner(url)['risk_score']





