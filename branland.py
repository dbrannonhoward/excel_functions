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
    col = "A"
    row = "3"
    misc_filename = "potato_beans"
    thing_to_write = "butts"
    # testing if i can create an excel file, name it, save it, close it
    tf = TestingFunctions()
    tf.create_new_excel_workbook_using_existing_class(misc_filename)
    # now seeing if i can re-open the same file, write to it and read from it
    excel = ExcelFile()
    excel.open_existing_workbook(misc_filename)
    excel.write_cell_value(col, row, thing_to_write)
    excel.save_changes()
    print("the cell value of {}{} is {}".format(col, row, excel.read_cell_value(col, row)))
