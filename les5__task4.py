"""
Домашнее задание:

38. *Создайте программу для игры с конфетами человек против человека.

Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота

b) Подумайте как наделить бота "интеллектом"

"""

import random


def play_game(total, correct_candy, players): 
    player_choice = 0
    progress = 1
    print(f'По результатам жеребьевки начинает игрок: {random.choice(players)}')
    while total > 0:
        print(f'{players[player_choice % 2]} возьмите конфеты')
        move = int(input(f'Ход №{progress} - {players[player_choice % 2]} сколько конфет вы забираете? '))
        if move > correct_candy or move <= 0:
            print('Вы ввели не корректное значение')
            continue
        else:
            total -= move
        
        if total > 0:
            print(f'Осталось {total} конфет')
        else:
            print('Конфеты разобраны')
        progress += 1 
        player_choice += 1
    return players[not player_choice % 2]


print('Вас приветствует игра "Конфеты!"')

player_1 = "Maks" # input('первый игрок введите ваше имя\n')
player_2 = "Ira" # input('второй игорок введите ваше имя\n')
players = [player_1, player_2]

# player_choice = random.randint(1, 2)
# print(player_choice)

# if player_choice == 1:
# 	print('Ход первого игрока')
# else:
# 	print('Ход второго игрока')
user_win = play_game(2021, 28, players)
print(f'Поздравляю! все конфеты достаются {user_win}! !')






# 2021 % 29 = 20