from excel_functions import *
from CONSTANTS import *
from math_stuff import *


def initialize_excel_object(filename):
    excel_file = ExcelFile(filename)
    return excel_file


def perform_tests(excel_file: ExcelFile):
    write_random_values(excel_file)


def write_random_values(excel_file: ExcelFile):
    for letter in ALPHABET_UPPER:
        for number in DIGITS:
            excel_file.write_cell_value(letter,
                                        number,
                                        str(get_random_three_digit_number()))


def main():
    excel_object = initialize_excel_object("sample_file.xlsx")
    perform_tests(excel_object)


main()
