per_cent = {'TBK': 5.6, 'SKB': 5.9, 'VTB': 4.28, 'SBER': 4.0}
deposit = input("Введите сумму депозита: ")
result = (int(int(deposit)*per_cent['TBK']/100),
      int(int(deposit)*per_cent['SKB']/100), int(int(deposit)*per_cent['VTB']/100),
      int(int(deposit)*per_cent['SBER']/100))
print('Депозит = ', result, 'Максимальная сумма, которую вы можете заработать', max(result))
