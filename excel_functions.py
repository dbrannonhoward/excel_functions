import openpyxl
from os import getcwd
import pathlib2


class ExcelFile:
    def __init__(self, filename: str):
        try:
            self.filename = self.get_filename_with_full_path(filename)
            self.workbook = openpyxl.load_workbook(self.filename)
            self.worksheet = self.workbook.active
        except RuntimeError:
            raise RuntimeError

    def cell_contains(self, col: str, row: str, search_term: str) -> bool:
        try:
            cell_value = self.read_cell_value(col, row)
            if cell_value is not None:
                if search_term in cell_value:
                    return True
            return False
        except RuntimeError:
            raise RuntimeError

    def cell_is_empty(self, col: str, row: str) -> bool:
        try:
            cell_value = self.read_cell_value(col, row)
            if cell_value is None:
                return True
            return False
        except RuntimeError:
            raise RuntimeError

    def get_all_sheet_names(self) -> list:
        list_of_sheet_titles = list()  # initialize an empty list
        try:
            for sheet in self.workbook:
                list_of_sheet_titles.append(sheet.title)
            return list_of_sheet_titles
        except RuntimeError:
            raise RuntimeError

    @staticmethod
    def get_current_working_directory() -> str:
        try:
            return getcwd()
        except RuntimeError:
            raise RuntimeError

    def get_filename_with_full_path(self, filename: str) -> str:
        try:
            return str(pathlib2.PurePath(self.get_current_working_directory(), filename))
        except RuntimeError:
            raise RuntimeError

    def read_cell_value(self, col: str, row: str) -> str:
        cell = col + row
        try:
            value = self.worksheet[cell].value
            return value
        except RuntimeError:
            raise RuntimeError

    def save_changes(self):
        try:
            self.workbook.save(self.filename)
        except RuntimeError:
            raise RuntimeError

    @staticmethod
    def valid_row(row: str) -> bool:
        try:
            if int(row) > 0:
                return True
            return False
        except RuntimeError:
            raise RuntimeError

    def write_cell_value(self, col: str, row: str, value: str):
        cell = col + row
        if self.valid_row(row):
            try:
                self.worksheet[cell] = value
            except RuntimeError:
                raise RuntimeError
