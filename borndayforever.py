year = int(input('В каком году родился Пушкин?: '))
while year != 1799:
    year = int(input('Неверно, попробуйте еще раз: '))
day = input('Верно, а в какой день?: ')
while day != '6 июня' and day != '6.06':
    day = input('Неверно, попробуйте еще раз: ')

print('Верно!')