"""
39. *Создайте программу для игры в "Крестики-нолики".

"""


# определение игроков
print("Первый игрок") 
player_1 = input("Введите имя первого игорока: ") 
  
print("Второй игрок") 
player_2 = input("Введите имя второго игорока: ")

# рисование доски
def get_board(board):
    for i in range(3):
      print(board[i * 3], "|", board[1 + i * 3], "|", board[2 + i * 3])
      print('----------')


board = range(9)
print(get_board(board))
