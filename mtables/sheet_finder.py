import pandas as pd
from configs import config
from mtables import fileselector


def getsheetname(full_filename, sheet_name_elements: list = config.sheet_name_elements):
    """

    :param full_filename:
    :param sheet_name_elements:
    :return: str first of sheet names with any sheet_name_element
    """
    with pd.ExcelFile(full_filename) as xl:
        for _sheet_name in xl.sheet_names:
            if fileselector.test_whitelist(_sheet_name, config.sheet_name_elements):
                return _sheet_name
