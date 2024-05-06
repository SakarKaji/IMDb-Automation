# from browser import BrowserComponent
# from excel_reader import Excel
# from connect_database import DatabaseComponent
# from qrlib.QRProcess import QRProcess

# class Process(QRProcess):
#     def __init__(self) -> None:
#         super().__init__()
#         self.browser_component = BrowserComponent()
#         self.register(self.browser_component)
        
#         self.database_component = DatabaseComponent()
#         self.register(self.browser_component)
        
#         self.excelreader_component = Excel()
#         self.register(self.excelreader_component)

#         self.data = None
        
  
    
#     def before_run(self):
#         self.browser_component.open_browser()
#         self.data = self.excelreader_component.read_excel()
#         self.database_component.create_table()
                    
    
    
#     def before_run_item(self, *args, **kwargs):
#     # Get run item created by decorator. Then notify to all components about new run item.
#     # run_item: QRRunItem = kwargs["run_item"]
#         pass

#     def execute_run_item(self, movie):
#         # Get run item created by decorator. Then notify to all components about new run item.

#         record= self.browser_component.search_bar(movie["Movie"])
#         self.database_component.insert_data(record)


       

#     def after_run_item(self, *args, **kwargs):
#         # Get run item created by decorator. Then notify to all components about new run item.
#         pass


    
#     # def run_process(self):
#         # self.browser.search_bar()
    
#     def after_run(self):
#         self.browser_component.close_browser()



#     def execute_run(self):
#         for movie in self.data:
#             self.before_run_item()
#             self.execute_run_item(movie)
#             self.after_run_item()
import time
from qrlib.QRProcess import QRProcess
from qrlib.QRDecorators import run_item
from qrlib.QRRunItem import QRRunItem
from browser import BrowserComponent
from connect_database import DatabaseComponent
from excel_reader import Excel
from qrlib.QREnv import QREnv

from robot.libraries.BuiltIn import BuiltIn

class Process(QRProcess):

    def __init__(self):
        super().__init__()
        # self.default_component = DefaultComponent()
        self.browser_component = BrowserComponent()
        self.register(self.browser_component)

        self.database_component = DatabaseComponent()
        self.register(self.database_component)
        
        self.excelreader_component = Excel()
        self.register(self.excelreader_component)

        # self.notify(run_item)


        # for i in range(1,100):
        #     run_itself.excelreader_component = ExcelReaderComponent()
        

        # # self.register(self.default_component)

        self.data = None
        # self.cred = QREnv.VAULTS['Movie_Scrapper']['url']

    @run_item(is_ticket=False)
    def before_run(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        # run_item: QRRunItem = kwargs["run_item"]
        # sem.logger.info(i)
        #     time.sleep(1)
        # self.default_component.login()
        self.browser_component.open_browser()
        self.data = self.excelreader_component.read_excel()
        self.database_component.create_table()

        # self.data = ["a", "b"]

    @run_item(is_ticket=False, post_success=False)
    def before_run_item(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)
        pass

    @run_item(is_ticket=False)
    def execute_run_item(self, movie,*args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)
        # BuiltIn().log_to_console(movie)
        record= self.browser_component.search_bar(movie)
        # BuiltIn().log_to_console("heRE---------------------------------")
        self.database_component.insert_data(record)
        # BuiltIn().log_to_console("heRE---------------------------------")

        # run_item.report_data["test"] = args[0]
        pass

    @run_item(is_ticket=False, post_success=False)
    def after_run_item(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)
        pass

    @run_item(is_ticket=False, post_success=False)
    def after_run(self, *args, **kwargs):
        # Get run item created by decorator. Then notify to all components about new run item.
        run_item: QRRunItem = kwargs["run_item"]
        self.notify(run_item)

        self.browser_component.close_browser()
        self.database_component.close_database()
    


        # self.default_component.logout()
 
    def execute_run(self):
        for movie in self.data:
            run_item =QRRunItem()

            self.before_run_item()
            self.execute_run_item(movie)
            self.after_run_item()