
import pprint
import requests
import json 

class Client(object):

    def __init__(self) -> None:
        self.url1 = "https://api.ipify.org/?format=json"
        self.url2 = "https://ipinfo.io/"
        self.url2suf = "/geo"

    def get_api(self, url):
        result = requests.get(url)
        dades = json.loads(result.text)
        return dades

    def get_myip(self):
        dades = self.get_api(self.url1)
        return dades["ip"]
    
    def get_info(self, ip):
        dades = self.get_api(self.url2+ip+self.url2suf)
        return dades

    def get_data(self):
        # descarregar-se dades
        myip = self.get_myip()
        # llegir xml
        dades = self.get_info(myip)
        # retornar dades
        return dades

if __name__=="__main__":
    client = Client()
    dades = client.get_data()
    pprint.pprint(dades)