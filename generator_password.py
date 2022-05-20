import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
passw = list()


def generate_password(length, chars):
    password = random.sample(chars, length)
    return password


# Настройка пароля
length = int(input(f'Введите длину генерируемого пароля: '))
amount = int(input(f'Введите количество необходимых паролей: '))
chars_dig = input(f'В пароле использовать цифры? (y - да, n - нет) ')
chars_low = input(f'В пароле использовать буквенные символы нижнего регистра?(y - да, n - нет) ')
chars_upp = input(f'В пароле использовать буквенные символы верхнего регистра? (y - да, n - нет) ')
chars_pun = input(f'В пароле использовать знаки пунктуации? (y - да, n - нет) ')
chars_del = input(f'Исключать неоднозначные символы il1LoO0? (y - да, n - нет) ')

if chars_dig == 'y':
    chars += digits
if chars_low == 'y':
    chars += lowercase_letters
if chars_upp == 'y':
    chars += uppercase_letters
if chars_pun == 'y':
    chars += punctuation
if chars_del == 'y':
    for i in 'il1LoO0':
        chars = chars.replace(i, '')

for _ in range(amount):
    password = generate_password(length, chars)
    passw.append(''.join(password))

print('Список паролей:', *passw, sep='\n')