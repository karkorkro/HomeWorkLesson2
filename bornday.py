year = int(input('В каком году родился Пушкин?: '))
if year == 1799:
    day = input('A какого числа?: ')
    if day == '6 июня' or day == '6.06':
        print('Верно!')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год рождения!')