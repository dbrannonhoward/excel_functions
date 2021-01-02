from excel_functions import *
from datetime import datetime

import os

class WesTest:
    def __init__(self):
        pass
    def create_excel_workbook(self, sheet_name):
        #created_sheet = WesTest.create_excel_workbook(sheet_name)
        if ExcelFile.create_empty_excel_workbook_named_(sheet_name):
            print('Creation of ' + sheet_name + ' SUCCESS!!!')
        else:
            print('you FAILED to create ' + sheet_name + '!')
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
    def copy_excel_cell_from_one_sheet_to_another(self, sheet_one, s1col, s1row, sheet_two, s2col, s2row):
        excel = ExcelFile()
        excel.open_existing_workbook(sheet_one)
        read_cell = excel.read_cell_value(s1col, s1row)
        read_cell = str(read_cell)
        if read_cell == '7052':
            copied_cell = read_cell
            print('read cell ' + read_cell)
            print('copied cell ' + copied_cell)
            excel.open_existing_workbook(sheet_two)
            excel.write_cell_value(s2col, s2row, copied_cell)
            excel.save_changes()
        else:

            return
        # copied_cell = excel.read_cell_value(col, row)
        # excel.save_changes()
        # excel.open_existing_workbook(sheet_two)
        # #print(copied_cell)
        # excel.write_cell_value(col, row, copied_cell)
        # excel.save_changes()

if __name__ == '__main__':
    today = datetime.today().strftime('%d_%b_%Y')
    wt = WesTest()
    excel = ExcelFile()
    todayWarrantyFile = 'WarrantyClaims' + today)
    wt.create_excel_workbook(todayWarrantyFile)
    excel.open_existing_workbook(todayWarrantyFile)




    # wt = WesTest()
    # excel_being_copied = 'tomato'
    # excel_being_pasted = 'zuccini'
    # s1col = 'A'
    # s1row = '4'
    # s2col = 'B'
    # s2row = '3'
    # wt.copy_excel_cell_from_one_sheet_to_another(excel_being_copied, s1col, s1row, excel_being_pasted, s2col, s2row)



    # wt = WesTest()
    # wt.create_excel_workbook(excel_being_copied)
    # wt.create_excel_workbook(excel_being_pasted)
    # wt.open_existing_excel_workbook_creates_array_of_cell_values(100, 26)
    # wt.copy_excel_cell_from_one_sheet_to_another(excel_being_copied, excel_being_pasted)
