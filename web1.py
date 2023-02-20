
import urllib3

class Client(object):

    def __init__(self) -> None:
        self.url = "https://www.99-bottles-of-beer.net/language-python-808.html"
    
    def get_web(self):
        # connect url
        httppool = urllib3.PoolManager()
        # get html
        resultat = httppool.request("GET", self.url)
        # retorn html
        return resultat.data.decode('utf-8')
        

    def get_data(self):
        # descarregar-se web
        dades = self.get_web()
        # llegir html
        # retornar dades
        return dades

if __name__=="__main__":
    client = Client()
    dades = client.get_data()
    print(dades)