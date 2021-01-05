from pocket import Coin
import os
import pathlib2
import time
from excel_functions import ExcelFile
penny = Coin()


class BetterExcelFile(ExcelFile):
    def __init__(self):
        super().__init__()

    def create_new_workbook(self):
        try:
            self.create_empty_excel_workbook_named_('test_file.xlsx')
        except OSError:
            raise OSError


class Directories:
    def __init__(self, debug=False):
        self.cwd = self.get_current_working_directory()
        self.cwd_full_path = self.get_full_path_to_current_working_directory()
        self.cwd_full_path_parts = self.get_list_of_all_parent_directories()
        self.username = self.get_active_user_username()
        if debug:
            self._debug()

    @staticmethod
    def get_current_working_directory() -> str:
        wait_one_second()
        print('try to get cwd')
        try:
            cwd = os.getcwd()
            if not isinstance(cwd, str):
                print('cwd is not a string! exiting program')
                raise TypeError
            print('getcwd success!')
            return cwd
        except OSError:
            raise OSError

    def get_full_path_to_current_working_directory(self) -> pathlib2.Path:
        wait_one_second()
        print('try to get full path to cwd')
        required_type = pathlib2.Path
        try:
            cwd_converted_to_path_object = required_type(self.cwd)
            if not isinstance(cwd_converted_to_path_object, required_type):
                print('cwd_converted_to_path_object is not {}! exiting program'.format(required_type))
                raise TypeError
            full_path_to_current_working_directory = \
                pathlib2.Path.resolve(cwd_converted_to_path_object)
            print('get full path success!')
            return full_path_to_current_working_directory
        except OSError:
            raise OSError

    def get_list_of_all_parent_directories(self) -> list:
        wait_one_second()
        parent_directories = list()
        print('try to get list of all parent directories')
        try:
            for parent_dir in self.cwd_full_path.parts:
                wait_one_second()
                print('found {}, adding to {}!'.format(parent_dir, parent_directories))
                parent_directories.append(parent_dir)
            print('get list of all parent directories success!')
            return parent_directories
        except OSError:
            raise OSError

    def get_active_user_username(self) -> str:
        wait_one_second()
        print('try to get active user\'s username')
        if self.system_is_linux():
            try:
                username = self.cwd_full_path_parts[2]
                if not isinstance(username, str):
                    print('{} is not a string! exiting program'.format(username))
                    raise TypeError
                print('get username for {} success!'.format(username))
                return username
            except IndexError:
                raise IndexError

    @staticmethod
    def system_is_linux() -> bool:
        wait_one_second()
        print('try to find out what operating system user has..')
        search_string = 'ix'
        try:
            os_name = os.name
            print('found os name {}!'.format(os_name))
            if search_string in os_name:
                print('success!')
                return True
            print('this isn\'t linux, what a stupid!')
            insult_string = 'you are stupid!'
            for i in range(999):
                print(return_string_with_random_capitalization(insult_string))
                time.sleep(0.08)
            return False
        except OSError:
            raise OSError

    def _debug(self):
        print('your username is {}'.format(self.get_active_user_username()))


def return_string_with_random_capitalization(string: str) -> str:
    insult_string = list()
    for letter in string:
        if letter.isalpha():
            penny.flip()
            state = penny.state
            if state:
                insult_string.append(letter.upper())
            else:
                insult_string.append(letter.lower())
        else:
            insult_string.append(letter)
    return ''.join(insult_string)


def wait_one_second():
    time.sleep(1)


if __name__ == '__main__':
    directory = Directories(debug=True)
    bef = BetterExcelFile()
    pass
