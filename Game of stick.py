sticks = int(input('введите количество палочек : '))
player1 = str(input('введите имя игрока 1 : '))
player2 = str(input('введите имя игрока 2 : '))
gamer = player1
while sticks > 0:
    print(f'осталось палочек {sticks}')
    turn = int(input(f'ход игрока {gamer} введите кол-во палочек (от 1 до 3) : '))
    if turn < 1 or turn > 3:
        break
    sticks -= turn
    gamer = player2 if gamer == player1 else player1
print(f'победитель {gamer}')
