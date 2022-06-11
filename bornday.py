birthday = '6 июня'
year = int(input('А вы знаете год рождения А.С.Пушкина?: '))
if year == 1799:
    birthday_people = input('А день рождения?: ')
    if birthday_people == birthday:
        print('Верно')
    else:
        print('Неверный день рождения')
else:
    print('Неверный год')
