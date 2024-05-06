from RPA.Excel.Files import Files
from constants import excel_file
from qrlib.QRComponent import QRComponent

# import pandas as pd


class Excel(QRComponent):
    def __init__(self) -> None:
        super().__init__()
        pass
    
    def read_excel(self):
        self.lib = Files()
        self.lib.open_workbook(excel_file)
        data = self.lib.read_worksheet_as_table(header=True)
        # for row in data:
            # print(data)
        return data

        # try:
        #     movies = pd.read_excel(excel_file)
        #     return movies['Movie']
        # except Exception as ex:
        #     raise ex


