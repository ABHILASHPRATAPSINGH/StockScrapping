import pandas
import openpyxl

from utility import PathUtility


class ImportExportData:

    def importDataToExcel(self, datafrm):
        self.datafrm = datafrm
        df: pandas.DataFrame = pandas.DataFrame(self.datafrm)
        # df.to_excel(r"C:\Users\DELL\Desktop\abhi.xlsx")

    def importStock_URL(self):
        filePath=PathUtility.getPackagedFilePathStrict("resource","Market watch.xlsm")
        stockes = pandas.read_excel(filePath, sheet_name="All", skiprows=6)
        # stockes = pandas.read_excel(r"C:\Users\DELL\Desktop\Market watch.xlsm", sheet_name="All", skiprows=6)
        df = stockes.loc[:, ['Stokes', 'URL']]
        df.dropna(inplace=True)
        df = df.set_index('Stokes')
        df = df.replace('https://www.financialexpress.com', 'NA')
        df = df[df['URL'] != 'NA']
        return df