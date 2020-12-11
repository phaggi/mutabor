import os
from pprint import pprint
from tkinter import Tk, filedialog
from pathlib import Path

from configs import config

my_file_types = config.file_types
my_black_list = config.blacklist
my_white_list = config.whitelist
numfil = config.numfil


def walk_level(some_dir: str or Path):
    some_dir = Path(some_dir)
    file_list = set()
    with os.scandir(some_dir) as it:
        for entry in it:
            if not entry.name.startswith('.') and entry.is_file():
                file_list.update({entry.name})
    return sorted(list(file_list))


def find_words_parts(words: list or str, words_parts: list):
    """
    :return list:
    :param words: word or list of words
    :type words_parts: list of 'bad' words
    """
    if isinstance(words, str):
        words = [words]
    return [any(part.lower() in word.lower() for part in words_parts) for word in words]


def select_folder():
    root = Tk()
    root.withdraw()
    return Path(filedialog.askdirectory())


def make_file_list(file_types: list,
                   blacklist: list,
                   whitelist: list,
                   folder: str = ''):
    """

    :param folder: optional (str or Path)
    :param whitelist: whitelist of good words (str)
    :param blacklist: blacklist of fool words (str)
    :param file_types: list of types of files (str)
    :return: tuple: folder, sorted list of files in folder, with type in file_types and without blacklist in name
    """
    if not folder:
        folder = Path(select_folder())
    else:
        folder = Path(folder)
    file_list = set()
    for filename in walk_level(folder):
        filename_parts = filename.split('.')
        if len(filename_parts) > 1:
            file_type = filename_parts[len(filename_parts) - 1]
            if (file_type in file_types) \
                    and not any(find_words_parts(filename, blacklist)) \
                    and any(find_words_parts(filename, whitelist)):
                file_list.update({folder / filename})
    return sorted(list(file_list)), folder


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
    print(any(find_words_parts('test', ['test'])))
    pprint(f'walk: {walk_level("/Users/phaggi/Documents/_test")}')
    my_file_list, _ = make_file_list(file_types=my_file_types,
                                     blacklist=my_black_list,
                                     whitelist=my_white_list,
                                     folder=Path('/Users/phaggi/Documents/_test'))
    pprint(f'file_list:{my_file_list}')
    pprint(make_file_dict(file_list=my_file_list, num_fil=numfil))
