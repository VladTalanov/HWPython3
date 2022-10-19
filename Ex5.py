# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21, 13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

number = int(input('Enter the number: '))
def fibonacci(num):
    fbncc = []
    n1, n2 = 1, 1
    for _ in range(num):
        fbncc.append(n1)
        n1, n2 = n2, n1 + n2
    n1, n2 = 0, 1
    for _ in range(num+1):
        fbncc.insert(0, n1)
        n1, n2 = n2, n1 - n2
    return fbncc
print(fibonacci(number))