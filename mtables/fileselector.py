import os
from pprint import pprint
from tkinter import Tk, filedialog

from configs import config


def walk_level(some_dir):
    file_list = set()
    with os.scandir(some_dir) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                file_list.update({entry.name})
    return sorted(list(file_list))


def test_blacklist(string: str, blacklist: list):
    """
    :return bool: True if all element from whitelist is not in string
    :param string: str name of file
    :type blacklist: list of 'bad' words
    """
    result = True
    for bad_words in blacklist:
        if bad_words in string:
            result = False
    return result


def test_whitelist(string: str, whitelist: list):
    """
    :return bool: True if any element from whitelist is in string
    :param string: str name of file
    :param whitelist: list of 'good' words
    """
    result = False
    for good_words in whitelist:
        if good_words not in string:
            result = True
    return result


def select_folder():
    root = Tk()
    root.withdraw()
    return filedialog.askdirectory()


def make_file_list(file_types: list = config.file_types,
                   blacklist: list = config.blacklist,
                   whitelist: list = config.whitelist):
    """

    :param whitelist: whitelist of good words (str)
    :param blacklist: blacklist of fool words (str)
    :param file_types: list of types of files (str)
    :return: sorted list of files in folder, with type in file_types and without blacklist in name
    """
    folder_selected = select_folder()
    file_list = set()
    for filename in walk_level(folder_selected):
        filename_parts = filename.split('.')
        if len(filename_parts) > 1:
            file_type = filename_parts[len(filename_parts) - 1]
            if file_type in file_types and test_blacklist(filename, blacklist) and test_whitelist(filename, whitelist):
                file_list.update({filename})
    return sorted(list(file_list))


if __name__ == '__main__':
    pprint(make_file_list())
