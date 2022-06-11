year = int(input('А вы знаете год рождения А.С.Пушкина?: '))
while year != 1799:
    year = int(input('Еще раз попробуйте: '))
if year == 1799:
    print('Верно')