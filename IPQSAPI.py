import json
import requests
import urllib


# You may need to install Requests pip
# python -m pip install requests

class IPQS:
        key = 'fi4mcakq7erKrWA3aW4CmGIxqcOuWkSk'

        def malicious_url_scanner_api(self,url):
                url = 'https://www.ipqualityscore.com/api/json/url/%s/%s' % (self.key, urllib.parse.quote_plus(url))
                x = requests.get(url)
                return (json.loads(x.text))

        def isUnsafe(self,url):
                return self.malicious_url_scanner_api(url)['unsafe']

        def isSpamming(self,url):
                return self.malicious_url_scanner_api(url)['spamming']

        def isMalware(self,url):
                return self.malicious_url_scanner_api(url)['malware']

        def isPhishing(self,url):
                return self.malicious_url_scanner_api(url)['phishing']

        def isSuspicious(self,url):
                return self.malicious_url_scanner_api(url)['suspicious']

        def isAdult(self,url):
                return self.malicious_url_scanner_api(url)['adult']

        def getRiskScore(self,url):
                return self.malicious_url_scanner_api(url)['risk_score']


#ipqs = IPQS()
#result = ipqs.malicious_url_scanner_api()





