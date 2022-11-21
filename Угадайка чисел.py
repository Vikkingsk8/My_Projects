import random


trying = 0
enigma = random.randint(1, 50)
while trying < 6:
    number = int(input('Введите число: '))
    trying += 1
    if number < enigma:
        print('Вы ввели число меньше числа загаданного компьютером')
        continue
    if number > enigma:
        print('Вы ввели число больше числа загаданного компьютером')
        continue
    if number == enigma:
        print('Вы угадали, поздравляю!!!')
        trying -= 1
        break
if trying == 6:
    print('Вы проиграли, попробуйте еще раз')

