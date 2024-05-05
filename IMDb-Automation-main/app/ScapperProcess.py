from browser import BrowserComponent
from excel_reader import Excel
from connect_database import DatabaseComponent
from qrlib.QRProcess import QRProcess

class Process(QRProcess):
    def __init__(self) -> None:
        super().__init__()
        self.browser_component = BrowserComponent()
        self.register(self.browser_component)
        
        self.database_component = DatabaseComponent()
        self.register(self.browser_component)
        
        self.excelreader_component = Excel()
        self.register(self.excelreader_component)

        self.data = None
        
  
    
    def before_run(self):
        self.browser_component.open_browser()
        self.data = self.excelreader_component.read_excel()
        self.database_component.create_table()
                    
    
    
    def before_run_item(self, *args, **kwargs):
    # Get run item created by decorator. Then notify to all components about new run item.
    # run_item: QRRunItem = kwargs["run_item"]
        pass

    def execute_run_item(self, movie):
        # Get run item created by decorator. Then notify to all components about new run item.

        record= self.browser_component.search_bar(movie["Movie"])
        self.database_component.insert_data(record)


       

    def after_run_item(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        pass


    
    # def run_process(self):
        # self.browser.search_bar()
    
    def after_run(self):
        self.browser_component.close_browser()



    def execute_run(self):
        for movie in self.data:
            self.before_run_item()
            self.execute_run_item(movie)
            self.after_run_item()
