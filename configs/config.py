result_filename = '_result'
result_filetype = 'xlsx'
file_types = ['xls', 'xlsx']
blacklist = ['result', 'сборка']  # list of fool words (str)
numfil = {'Белг': 0,
          'БО': 1,
          'Брянск': 1,
          'Орел': 1,
          'Орло': 1,
          'ВИ': 2,
          'Владимир': 2,
          'Иванов': 2,
          'Воронеж': 3,
          'Калу': 4,
          'Курск': 5,
          'Липецк': 6,
          'ТР': 7,
          'Рязан': 7,
          'Тул': 7,
          'Смоленск': 8,
          'Тамбов': 9,
          'Твер': 10,
          'ЯК': 11,
          'Ярослав': 11,
          'Костр': 11}
filnumdict = {0: 'Белгородский',
              1: 'Брянск-Орел',
              2: 'Владимир-Иваново',
              3: 'Воронежский',
              4: 'Калужский',
              5: 'Курский',
              6: 'Липецкий',
              7: 'Смоленский',
              8: 'Тамбовский',
              9: 'Тверской',
              10: 'Тула-Рязань',
              11: 'Ярославль-Кострома'}

filnumb = {0: ['Белг'],
           1: ['БО', 'Брянск', 'Орел', 'Орл'],
           2: ['ВИ', 'Владимир', 'Иванов'],
           3: ['Воронеж'],
           4: ['Калуг', 'Калуж'],
           5: ['Курск'],
           6: ['Липецк'],
           7: ['ТР', 'Рязан', 'Тул'],
           8: ['Смоленс'],
           9: ['Тамбов'],
           10: ['Твер'],
           11: ['ЯК', 'Яросл', 'Костр']}
whitelist = numfil.keys()
sheet_name_elements = ['нараст']
