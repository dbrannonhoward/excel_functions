from openpyxl import load_workbook
from pathlib2 import PurePath
import os


class ExcelFile:
    def __init__(self, filename: str):
        try:
            self.filename = self.get_filename_with_full_path(filename)
            self.workbook = load_workbook(self.filename)
            self.worksheet = self.workbook.active
        except RuntimeError:
            raise RuntimeError

    def cell_contains(self, col: str, row: str, search_term: str) -> bool:
        try:
            cell_value = self.read_cell_value(col, row)
        except RuntimeError:
            raise RuntimeError
        if cell_value is not None:
            if search_term in cell_value:
                return True
        return False

    def cell_is_empty(self, col: str, row: str) -> bool:
        try:
            cell_value = self.read_cell_value(col, row)
        except RuntimeError:
            raise RuntimeError
        if cell_value is None:
            return True
        return False

    def get_all_sheet_names(self) -> list:
        list_of_sheet_titles = list()  # initialize an empty list
        for sheet in self.workbook:
            list_of_sheet_titles.append(sheet.title)
        return list_of_sheet_titles

    @staticmethod
    def get_current_working_directory() -> str:
        try:
            return os.getcwd()
        except RuntimeError:
            raise RuntimeError

    def get_filename_with_full_path(self, filename: str) -> str:
        try:
            return str(PurePath(self.get_current_working_directory(), filename))
        except RuntimeError:
            raise RuntimeError

    def read_cell_value(self, col: str, row: str) -> str:
        cell = col + row
        try:
            value = self.worksheet[cell].value
        except RuntimeError:
            raise RuntimeError
        return value

    def save_changes(self):
        try:
            self.workbook.save(self.filename)
        except RuntimeError:
            raise RuntimeError

    @staticmethod
    def valid_row(row: str) -> bool:
        if int(row) > 0:
            return True
        return False

    def write_cell_value(self, col: str, row: str, value: str):
        cell = col + row
        if self.valid_row(row):
            try:
                self.worksheet[cell] = value
            except RuntimeError:
                raise RuntimeError
        self.save_changes()
