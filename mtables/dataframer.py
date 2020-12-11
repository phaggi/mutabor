from pathlib import Path

from mtables import fileselector
from mtables import sheet_finder
from configs import config
import pandas as pd
import numpy as np
from mtables.sheet_finder import getsheetname

pd.set_option('use_inf_as_na', True)


def get_header(xl_df, word_in_header):
    try:
        result = xl_df.isin([word_in_header])
        my_series = result.any()
        col = list(my_series[my_series].index)[0]
        return list(result[col][result[col]].index)[0]
    except LookupError:
        return None


def get_df(filename, sheetname, word_in_header, _header=None):
    """

    :param filename:
    :param sheetname:
    :param word_in_header:
    :param _header:
    :return:
    """
    if not _header:
        xl = pd.read_excel(filename)
        _header = get_header(xl, word_in_header)
    if not _header:
        _header = 1
    df = pd.read_excel(filename, sheet_name=sheetname, header=_header)
    df.fillna(value='-', inplace=True)
    return df


'''def make_df(file_dict: dict, fil_numb, sheetnames, column_name, header=None):
    if not header:
        _header = 1
    dfprev = False
    for key in file_dict.keys():
        file = file_dict[key]
        sheet_name = getsheetname(full_filename=file, sheet_name_elements=sheetnames)
        print(sheet_name)
        search_for = '|'.join(fil_numb[key])
        my_df = pd.read_excel(file, sheet_name=sheet_name)  # , use_inf_as_na=False)
        print(type(my_df))
        my_df.replace(np.nan, 0, inplace=True)
        my_df.fillna(0, inplace=True)

        print(search_for)
        if isinstance(dfprev, bool):
            dfprev = my_df[my_df[column_name].str.contains(search_for, na=False)]
        else:
            dfnow = my_df[my_df[column_name].str.contains(search_for, na=False)]
        dfprev = pd.concat([dfprev, dfnow], sort=False)
    return dfprev'''


if __name__ == '__main__':
    numfil = config.numfil
    filetypes = config.file_types
    blacklist = config.blacklist
    whitelist = config.whitelist
    filnumb = config.filnumb
    sheet_names = config.sheet_name_elements
    my_folder = Path('/Users/phaggi/Documents/_test')
    filelist, folder = fileselector.make_file_list(file_types=filetypes, blacklist=blacklist, whitelist=whitelist,
                                                   folder=my_folder)
    filedict = fileselector.make_file_dict(file_list=filelist, num_fil=numfil)
    my_df = get_df(filename=Path('../tests/test.xlsx'), sheetname='testname', word_in_header='ИТОГО')
    # xl_df = make_df(file_dict=filedict, fil_numb=filnumb, sheetnames=['Лист 1'], column_name='ИТОГО')
    print(my_df.head())
