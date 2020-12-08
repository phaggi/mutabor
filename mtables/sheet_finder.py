import pandas as pd
from configs import config
from mtables import fileselector



def getsheetname(full_filename: str, sheet_name_elements: list = config.sheet_name_elements):
    """

    :param full_filename:
    :param sheet_name_elements:
    :return: str first of sheet names with any sheet_name_element
    """
    with pd.ExcelFile(full_filename) as xl:
        _sheet_name: str
        for _sheet_name in xl.sheet_names:
            if not fileselector.test_whitelist(_sheet_name, config.sheet_name_elements):
                continue
            assert isinstance(_sheet_name, str)
            return _sheet_name


if __name__ == '__main__':
    testname = getsheetname('../tests/test.xlsx', sheet_name_elements=['test'])
    print(f'test of getsheetname: test_name = \"{testname}\", {testname == "testname"}')
