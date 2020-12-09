from pprint import pprint
from pathlib import Path
from configs import config
from mtables import fileselector
from mtables import sheet_finder

if __name__ == '__main__':
    mypath = Path('/Users/phaggi/Documents/_test')
    filenames = fileselector.make_file_list(file_types=config.file_types,
                                            blacklist=config.blacklist,
                                            whitelist=config.whitelist,
                                            folder_selected=mypath)
    pprint(filenames)
    for file in filenames:
        print(f'found: {sheet_finder.getsheetname(file, ["Лист 1"])}')
    pprint(fileselector.make_file_dict(filenames, config.numfil))
