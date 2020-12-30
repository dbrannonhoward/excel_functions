from excel_functions import *
import os

class WesTest:
    def __init__(self):
        pass
    def create_excel_workbook(self, created_sheet):
        #created_sheet = WesTest.create_excel_workbook(created_sheet)
        if ExcelFile.create_empty_excel_workbook_named_(created_sheet):
            print('Creation SUCCESS')
        else:
            print('you FAILED')
    def open_existing_excel_workbook_creates_array_of_cell_values (self, num_of_row=1, num_of_col=100):
        excel = ExcelFile()
        excel.open_existing_workbook(excel_being_copied)
        for i in range(1, num_of_col+1):
            col = chr(ord('@')+i)
            for i in range(1, num_of_row+1):
                row = i
                row = str(row)
                #print(col + row)
                excel.write_cell_value(col, row, col+row)
        excel.save_changes()
    def copy_excel_cell_from_one_sheet_to_another(self, sheet_one, sheet_two):
        col = 'B'
        row = '5'
        excel = ExcelFile()
        excel.open_existing_workbook(sheet_one)
        copied_cell = excel.read_cell_value(col, row)
        excel.save_changes()
        excel.open_existing_workbook(sheet_two)
        #print(copied_cell)
        excel.write_cell_value(col, row, copied_cell)
        excel.save_changes()

if __name__ == '__main__':
    excel_being_copied = 'tomato'
    excel_being_pasted = 'zuccini'
    wt = WesTest()
    #wt.create_excel_workbook(excel_being_copied)
    #wt.create_excel_workbook(excel_being_pasted)
    #wt.open_existing_excel_workbook_creates_array_of_cell_values(1000, 26)
    wt.copy_excel_cell_from_one_sheet_to_another(excel_being_copied, excel_being_pasted)
