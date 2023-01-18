import bs4
import pandas




class ExtractData:

    def __init__(self, body: bs4.BeautifulSoup):
        self.body = body

    def exData(self) -> list:
        data_table = self.body.find(id='modality')
        sata = []
        for tr in data_table.find_all('tr'):
            mata = []
            for td in tr.find_all('td'):
                mata.append(td.text)
            sata.append(mata)
        return sata

    def ex_shareholding_details(self):
        soup = self.body
        trs = soup.find(class_='shareholdcnt')
        st = []
        for tr in trs.find_all('tr'):
            lst1 = []
            for td in tr.find_all('td'):
                print(td.text)
                lst1.append(td.text)
            st.append(lst1)
        return st

    def ex_share_financial_report(self):
        soup = self.body
        t = soup.find(class_='table-databox')
        trs = soup.find('tbody')
        st = []
        for tr in trs.find_all('tr'):
            lst1 = []
            for td in tr.find_all('td'):
                lst1.append(td.text)
            st.append(lst1)
        return st

    def ex_share_fundaments(self):
        soup = self.body

        st = []
        for span in soup.find_all('div', class_="trbox"):
            lst1 = []
            for td in span.find_all('span'):
                lst1.append(td.text)
            st.append(lst1)
        return st

    def stockes_list(self):
        stockes=pandas.read_excel(r"C:\Users\DELL\Desktop\Market watch.xlsm",sheet_name="all")
        return stockes

