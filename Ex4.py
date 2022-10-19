# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

number = int(input('Enter the number: '))
def binary(num):
    res = ''
    while num > 0:
        res = str(num % 2) + res
        num = num // 2
    return res
print(f'Binary: {binary(number)}')