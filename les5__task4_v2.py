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
    progress = 1
    play = random.choice(players)
    print(f'По результатам жеребьевки начинает игрок: {play}')
    if play == player_1:
        player_choice = 0
    else:
        player_choice = 1
    while total > 0:
        if players[player_choice % 2] is not player_2:
            move = int(input(f'Ход №{progress} - {player_1} сколько конфет вы забираете? '))
            print(f'Игрок {player_1} забрал {move} конфет') 
        if players[player_choice % 2] is not player_1:    
            if progress == 1 or total % 29 == 0:
                move = random.randint(1, 28)
            else:
                move = total % 29
            print(f'{players[player_choice % 2]} забрал {move} конфет')
        if move > correct_candy or move <= 0:
            print('Вы ввели не корректное значение, повторите ход')
            continue
        else:
            total -= move
        print(f'Осталось {total} конфет') if total > 0 else print('Конфеты разобраны')
        progress += 1 
        player_choice += 1    
    return players[not player_choice % 2]


print('Вас приветствует игра "Конфеты!"')

player_1 = "Maks" # input('первый игрок введите ваше имя\n')
player_2 = "Сomputer"
players = [player_1, player_2]

user_win = play_game(100, 28, players)
print(f'Поздравляю! все конфеты достаются {user_win}!')
