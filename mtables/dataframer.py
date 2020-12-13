import pandas as pd
import numpy as np
from pathlib import Path
from pprint import pprint
from mtables import fileselector
from configs import config

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
    df.replace(np.nan, '-', inplace=True)
    df.fillna(value='-', inplace=True)
    return df


def filter_df(df: pd.DataFrame, column_name: str, search_for: str):
    return df[df[column_name].str.contains(search_for, na=False)]


def concat_df(file_dict: dict, sheetname: str, columnname: str, fil_numb: dict, header: int):
    df_prev = False
    df_now = False
    for key, filename in file_dict.items():
        next_df = get_df(filename=filename, sheetname=sheetname, word_in_header=columnname, _header=header)
        search_for = '|'.join(fil_numb[key])
        if isinstance(df_prev, bool):
            df_prev = filter_df(df=next_df, column_name=columnname, search_for=search_for)
        else:
            df_now = filter_df(df=next_df, column_name=columnname, search_for=search_for)
            df_prev = pd.concat([df_prev, df_now], sort=False)
    return df_prev


def write_result(df: pd.DataFrame,
                 folder_selected: Path,
                 result_file_name: str,
                 result_file_type: str,
                 set_data: bool = None):
    if not set_data:
        set_data = False

    if set_data:
        data = str('2020.12.12')
        resultfilename = '.'.join([result_file_name, data.strip(), result_file_type])
    else:
        data = ''
        resultfilename = '.'.join([result_file_name, result_file_type])
    print(resultfilename)
    out_file_name = folder_selected/resultfilename
    print(out_file_name)
    try:
        xlWriter = pd.ExcelWriter(out_file_name, engine='xlsxwriter')
        workbook = xlWriter.book
        df.to_excel(xlWriter, encoding='utf-8', index=False, sheet_name='сборка')
        xlWriter.save()
        xlWriter.close()
        print('Файл ', out_file_name, ' сохранен')
    except IOError:
        print("Could not open file! Please close Excel!")

if __name__ == '__main__':
    numfil = config.numfil
    filetypes = config.file_types
    blacklist = config.blacklist
    whitelist = config.whitelist
    filnumb = config.filnumb
    sheet_names = config.sheet_name_elements
    names = ['Валеев', 'Петрова', 'Конахин']
    my_folder = Path('/Users/phaggi/PycharmProjects/mutabor/tests/данные от филиалов/Гермес')
    filelist, folder = fileselector.make_file_list(file_types=filetypes, blacklist=blacklist, whitelist=whitelist,
                                                   folder=my_folder)
    filedict = fileselector.make_file_dict(file_list=filelist, num_fil=numfil)
    pprint(filedict)
    myfile = list(filedict.items())[0][1]
    print(myfile)

    key = numfil['БО']
    search_for = '|'.join(filnumb[key])
    # my_df = get_df(filename=myfile, sheetname='Гермес свод', word_in_header='Филиал', _header=7)
    # filtered_df = filter_df(df=my_df, column_name='Филиал', search_for=search_for)
    result_df = concat_df(file_dict=filedict, sheetname='Гермес свод', columnname='Филиал', fil_numb=filnumb, header=7)
    write_result(result_df, folder, config.result_filename, config.result_filetype, set_data=True)
