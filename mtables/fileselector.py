import os
from pprint import pprint
from tkinter import Tk, filedialog
from pathlib import Path

from configs import config

file_types = config.file_types
blacklist = config.blacklist
whitelist = config.whitelist
numfil = config.numfil


def walk_level(some_dir: str or Path):
    some_dir = Path(some_dir)
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
    for bad_word in blacklist:
        if bad_word in string:
            result = False
    return result


def test_whitelist(string: str, whitelist: list):
    """
    :return bool: True if any element from whitelist is in string
    :param string: str name of file
    :param whitelist: list of 'good' words
    """
    result = False
    for good_word in whitelist:
        if good_word in string:
            result = True
    return result


def select_folder():
    root = Tk()
    root.withdraw()
    return Path(filedialog.askdirectory())


def make_file_list(file_types: list,
                   blacklist: list,
                   whitelist: list,
                   folder_selected: str = ''):
    """

    :param whitelist: whitelist of good words (str)
    :param blacklist: blacklist of fool words (str)
    :param file_types: list of types of files (str)
    :return: tuple: folder, sorted list of files in folder, with type in file_types and without blacklist in name
    """
    if not folder_selected:
        folder_selected = Path(select_folder())
    else:
        folder_selected = Path(folder_selected)
    file_list = set()
    for filename in walk_level(folder_selected):
        filename_parts = filename.split('.')
        if len(filename_parts) > 1:
            file_type = filename_parts[len(filename_parts) - 1]
            if (file_type in file_types) and test_blacklist(filename, blacklist) and test_whitelist(filename,
                                                                                                    whitelist):
                file_list.update({folder_selected/filename})
    return sorted(list(file_list))


def make_file_dict(file_list: list, num_fil: dict):
    file_dict = {}
    for file in file_list:
        is_number = False
        number = None
        for key in num_fil.keys():
            if key in str(file):
                is_number = True
                number = num_fil[key]
        if is_number:
            file_dict.update({number: file})
    return file_dict


if __name__ == '__main__':
    print(test_whitelist('test', ['test']))
    pprint(f'walk: {walk_level("/Users/phaggi/Documents/_test")}')
    my_file_list = make_file_list(file_types=file_types,
                                  blacklist=blacklist,
                                  whitelist=whitelist,
                                  folder_selected=Path('/Users/phaggi/Documents/_test'))
    pprint(f'file_list:{my_file_list}')
    pprint(make_file_dict(file_list=my_file_list, num_fil=numfil))
