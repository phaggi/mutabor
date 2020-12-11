import pandas as pd
from configs import config
from mtables import fileselector


def getsheetname(full_filename: str, sheet_name_elements: list = ['test']):
    """

    :param full_filename:
    :param sheet_name_elements:
    :return: str first of sheet names with any sheet_name_element, or return None.
    """
    with pd.ExcelFile(full_filename) as xl:
        for _sheet_name in xl.sheet_names:
            if any(fileselector.find_words_parts(_sheet_name, sheet_name_elements)):
                assert isinstance(_sheet_name, str)
                return _sheet_name
            else:
                return None


if __name__ == '__main__':
    test_name = getsheetname('../tests/test.xlsx', sheet_name_elements=['test'])
    print(f'test of getsheetname: test_name = \"{test_name}\", {test_name == "testname"}')
