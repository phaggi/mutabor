from pprint import pprint

from configs import config
from mtables import fileselector
from mtables import sheet_finder

if __name__ == '__main__':
    folder, filenames = fileselector.make_file_list()
    pprint(filenames)
    for file in filenames:
        print(f'finded: {sheet_finder.getsheetname("/".join([folder, file]), ["Лист 1"])}')
