import random

game = ['камень', 'ножницы', 'бумага']
while True:
    player = input('Введите камень, ножницы или бумага : ')
    computer = random.choice(game)

    if player == computer:
        print('Ничья')
    elif player == 'камень' and computer == 'ножницы':
        print('Камень бьет ножницы ,вы победили')
    elif player == 'бумага' and computer == 'камень':
        print('Бумага бьет камень, вы победили')
    elif player == 'ножницы' and computer == 'бумага':
        print('ножницы бьют бумагу, вы победили')
    else:
        print('Вы проиграли')

    again = input('Желаете продолжить? Выберете да или нет : ')
    if again != 'да':
        print('Надеюсь скоро сыграем еще')
        break


