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
    def open_existing_excel_workbook_creates_array_of_cell_values (self, num_of_row=1, num_of_col=100):
        excel = ExcelFile()
        excel.open_existing_workbook(my_name_for_my_excel_file)
        for i in range(1, num_of_col+1):
            col = chr(ord('@')+i)
            for i in range(1, num_of_row+1):
                row = i
                row = str(row)
                print(col + row)
                excel.write_cell_value(col, row, col+row)
        excel.save_changes()
    def copy_excel_cell_from_one_sheet_to_another(self, sheet_one):
        col = 'S'
        row = '20'
        excel = ExcelFile()
        excel.open_existing_workbook(sheet_one)
        excel.read_cell_value(col, row)







if __name__ == '__main__':
    my_name_for_my_excel_file = 'tomato'
    cell_entry = 'cell entry I made'
    wt = WesTest()
    #wt.create_excel_workbook(my_name_for_my_excel_file)
    #wt.open_existing_excel_workbook_creates_array_of_cell_values(1000, 26)
    wt.copy_excel_cell_from_one_sheet_to_another(my_name_for_my_excel_file)



    #excel = ExcelFile()
    #excel.open_existing_workbook(my_name_for_my_excel_file)