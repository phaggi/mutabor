result_filename = '_result.xlsx'
file_types = ['xls', 'xlsx']
blacklist = ['result', 'сборка']  # list of fool words (str)
numfil = {'елг': 0,
          'БО': 1,
          'рянск': 1,
          'рел': 1,
          'рло': 1,
          'ВИ': 2,
          'ладим': 2,
          'ван': 2,
          'орон': 3,
          'алу': 4,
          'урск': 5,
          'ипец': 6,
          'ТР': 7,
          'язан': 7,
          'ул': 7,
          'мол': 8,
          'амбов': 9,
          'вер': 10,
          'ЯК': 11,
          'росл': 11,
          'остр': 11}
whitelist = numfil.keys()
