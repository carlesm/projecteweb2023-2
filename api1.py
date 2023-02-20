#  http://export.arxiv.org/api/query?search_query=all:electron&start=0&max_results=10


class Client(object):

    def __init__(self) -> None:
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=10&search_query=all:"


    def get_data(self, query):
        # descarregar-se dades
        dades = self.get_api(query)
        # llegir xml
        dades = self.parse_xml(dades)
        # retornar dades
        dades = self.select_data(dades)
        return dades

if __name__=="__main__":
    client = Client()
    dades = client.get_data("lstm")
    print(dades)