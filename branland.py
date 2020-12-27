from excel_functions import *


class TestingFunctions:
    def __init__(self):
        pass

    def create_new_excel_workbook_using_existing_class(self, some_name):
        if ExcelFile.create_empty_excel_workbook_named_(some_name):
            print("creation successful!")
        else:
            print("creation not successful!")


if __name__ == '__main__':
    tf = TestingFunctions()
    tf.create_new_excel_workbook_using_existing_class("potato_beans")
    excel = ExcelFile()
    excel.open_existing_workbook("potato_beans")
    excel.write_cell_value("A", "3", "butts")
    excel.save_changes()
