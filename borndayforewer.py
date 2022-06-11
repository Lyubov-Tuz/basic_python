year = 1799
birthday = '6 июня'
year_people= int(input('А вы знаете год рождения А.С.Пушкина?: '))
while year_people != year:
    year_people = int(input('Еще раз попробуйте: '))
if year_people == year:
    birthday_people = input('А день рождения?: ')
    while birthday_people != birthday:
        birthday_people = input('Еще раз попробуй вспомнить день рождения: ')
    print('Верно')

