answer = input('Я хочу сыграть с тобой в игру... ')
while answer == 'да':
    score = 0
    wrong_answers = 0
    qu1 = int(input('В каком году родился Джигурда?: ')) #1961
    if qu1 == 1961:
        score += 1
    else:
        wrong_answers += 1
    qu2 = int(input('В каком году родился Зеленский?: ')) #1978
    if qu2 == 1978:
        score += 1
    else:
        wrong_answers += 1
    qu3 = int(input('В каком году родился Чингачгук?: ')) # вероятно 1726, но это не точно
    if qu3 == 1726:
        score += 1
    else:
        wrong_answers += 1
    qu4 = int(input('В каком году родился Иисус?: ')) # в нулевом
    if qu4 == 0:
        score += 1
    else:
        wrong_answers += 1
    qu5 = input('В каком году родился Антихрист?: ') # он еще не родился, но это не точно
    if qu5 == "он еще не родился":
        score += 1
    else:
        wrong_answers += 1
    print('Процент правильных ответов:', score/ 5 * 100)
    print('Процент неправильных ответов', wrong_answers / 5 * 100)
    answer = input('Хотите сыграть еще раз? ')
print('Okay')