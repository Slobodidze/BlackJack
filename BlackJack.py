import random

comp_total = 0
player_total = 0
gen = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 7: 7, 8: 8, 9: 9, 10: 10, 11: 'Туз', 12: 'Валет', 13: 'Дама', 14: 'Король'}
cost = {2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 7: 7, 8: 8, 9: 9, 10: 10, 11: 11, 12: 10, 13: 10, 14: 10}

# Функция Выдачи карты Игроку
def player_card(total):
    player_choice = random.randint(2, 14)  # Генерируем
    player_name = gen[player_choice]  # Преобразуем в название
    player_cost = cost[player_choice]  # Преобразуем в стоимость
    total = total + player_cost
    print(f'Вам выпало: {player_name}')
    print(f'сумма баллов у Вас: {total}')
    return total;
# Функция Выдачи карты Боту
def comp_card(total):
    comp_choice = random.randint(2, 14)  # Генерируем
    comp_name = gen[comp_choice]  # Преобразуем в название
    comp_cost = cost[comp_choice]  # Преобразуем в стоимость
    total = total + comp_cost
    print(f'Боту выпало: {comp_name}')
    print(f'сумма баллов у Бота: {total}')
    return total;
# Функция определения Победителя
def who_win():
    if comp_total == player_total:
        print('Ничья')
    elif player_total > comp_total:
        print('Победа Игрока')
    else:
        print('Победа бота')
    exit()
while True:
    print('Играем в BlackJack. Чтобы выйти напишите: выход.')
    player = input('Играем?:')
    if player == 'выход':
        exit()
    for m in range(0, 2, 1):
        comp_total = comp_card(total=comp_total)  # Вызываем функцию Выдачи карты Боту
        player_total = player_card(total=player_total)# Вызываем функцию Выдачи карты Игроку
    print(f'сумма баллов у бота: {comp_total}')
    if comp_total == 22 or player_total == 22:
        if comp_total == player_total:
            print('Ничья')
            exit()
        elif player_total == 22:
            print('Безусловная Победа Игрока')
            exit()
        else:
            print('Безусловная Победа бота')
            exit()
    elif comp_total == 21 or player_total == 21:
        if comp_total == player_total:
            print('Ничья')
            exit()
        else:
            print('Возможно сыграть в ничью')
    for m in range(0, 3, 1):
        if comp_total < player_total:
            comp_total = comp_card(total=comp_total)  # Вызываем функцию Выдачи карты Боту
            if comp_total > 21:
                print('У Бота Перебор. Победа Игрока.')
                exit()
        player = input('Будете тянуть ещё карту? Да\Нет')
        if player not in ['Да', 'Нет', 'да', 'нет', 'д', 'н']:
            print('Неправильный ввод!')
        else:
            if player == 'Нет' or player == 'нет' or player == 'н':
                if comp_total < player_total:
                    comp_total = comp_card(total=comp_total)  # Вызываем функцию Выдачи карты Боту
                    if comp_total > 21:
                        print('У Бота Перебор. Победа Игрока.')
                        exit()
                who_win()# Вызываем функцию определения Победителя
            if player == 'Да' or player == 'да' or player == 'д':
                player_total = player_card(total=player_total)# Вызываем функцию Выдачи карты Игроку
                if player_total > 21:
                    print('У вас Перебор. Вы проиграли.')
                    exit()
    who_win()# Вызываем функцию определения Победителя
print('Досвидания')
exit()
