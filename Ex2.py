# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 5, 6]
if len(list) % 2 == 0:
    result = [list[n] * list[-n - 1]
            for n in range(len(list)) if n - 1 < n / 2]
else:
    result = [list[n] * list[-n - 1]
            for n in range(len(list)) if n - 1 <= n / 2]
print(result)