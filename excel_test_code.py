from excel_functions import *
import os

class WesTest:
    def __init__(self):
        pass
    def create_excel_workbook(self, potato):
        if ExcelFile.create_empty_excel_workbook_named_(potato):
            print('Creation SUCCESS')
        else:
            print('you FAILED')
    def cell_array (self, num_of_row, num_of_col):
        num_of_row = 100
        num_of_col = 10
        for i in range(1, num_of_col+1):
            print (i)
            print(chr(ord('@')+i))



if __name__ == '__main__':
    my_name_for_my_excel_file = 'tomato'
    cell_entry = 'cell entry I made'
    wt = WesTest()
    wt.create_excel_workbook(my_name_for_my_excel_file)
    wt.cell_array(100, 10)
    excel = ExcelFile()
    excel.open_existing_workbook(my_name_for_my_excel_file)
    #excel.write_cell_value(col, row, cell_entry)