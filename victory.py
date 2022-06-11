# Викторина
pushkin = 1799 # А.С.Пушкин
lermontov = 1814 # М.Ю.Лермонтов
gogol = 1809 # Н.В.Гоголь
griboedov = 1795 # А.С.Грибоедов
esenin = 1895 # С.А.Есенин
correct_answer = 0 # верные ответы
mistake = 0 # неверные ответы

answer_push = int(input('А вы знаете год рождения А.С.Пушкина?: ')) # 1799
if answer_push == pushkin:
    correct_answer += 1
else:
    mistake += 1


answer_ler = int(input('Год рождения М.Ю.Лермонтова?: ')) # 1814
if answer_ler == lermontov:
    correct_answer += 1
else:
    mistake += 1

answer_gog = int(input('Год рождения Н.В.Гоголя?: ')) # 1809
if answer_gog == gogol:
    correct_answer += 1
else:
    mistake += 1

answer_gr = int(input('Год рождения А.С.Грибоедова?: ')) # 1795
if answer_gr == griboedov:
    correct_answer += 1
else:
    mistake += 1

answer_es = int(input('Год рождения С.А.Есенина?: ')) # 1895
if answer_es == esenin:
    correct_answer += 1
else:
    mistake += 1


print('Количество правильных ответов: ', correct_answer)
print('Количество ошибок: ', mistake)
print('Процент правильных ответов:', correct_answer * 100 / 5)
print('Процент неправильных ответов:', mistake * 100 / 5)

game = input('Начнем игру сначала? Да / нет ')
while game == 'Да' or game == 'да':
    correct_answer = 0
    mistake = 0

    answer_push = int(input('А вы знаете год рождения А.С.Пушкина?: '))  # 1799
    if answer_push == pushkin:
        correct_answer += 1
    else:
        mistake += 1

    answer_ler = int(input('Год рождения М.Ю.Лермонтова?: '))  # 1814
    if answer_ler == lermontov:
        correct_answer += 1
    else:
        mistake += 1

    answer_gog = int(input('Год рождения Н.В.Гоголя?: '))  # 1809
    if answer_gog == gogol:
        correct_answer += 1
    else:
        mistake += 1

    answer_gr = int(input('Год рождения А.С.Грибоедова?: '))  # 1795
    if answer_gr == griboedov:
        correct_answer += 1
    else:
        mistake += 1

    answer_es = int(input('Год рождения С.А.Есенина?: '))  # 1895
    if answer_es == esenin:
        correct_answer += 1
    else:
        mistake += 1

    print('Количество правильных ответов: ', correct_answer)
    print('Количество ошибок: ', mistake)
    print('Процент правильных ответов:', correct_answer * 100 / 5)
    print('Процент неправильных ответов:', mistake * 100 / 5)

    game = input('Начнем игру сначала? Да / нет ')
