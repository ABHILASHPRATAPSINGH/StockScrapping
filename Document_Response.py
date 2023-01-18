import bs4
import requests


class Document_Response:

    def __init__(self, url: str):
        self.url = url

    def htmlDocument(self) -> bs4.BeautifulSoup:
        with open(self.url, 'r') as mainURL:
            body = mainURL.read()
            soup = bs4.BeautifulSoup(body, 'html.parser')
        return soup

    def req_htmlDocument(self):
        hdr = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36 Edg/90.0.818.56"}
        resp = requests.get(self.url, headers=hdr)
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')
        return soup