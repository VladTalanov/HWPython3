# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

list = [1.1, 1.2, 3.1, 5, 10.01]
maxx, minn = 0, 1
for i in list:
    if (divmod(i, 1))[1] > maxx:
        maxx = divmod(i, 1)[1]
    elif (divmod(i, 1))[1] < minn and (divmod(i, 1))[1] != 0:
        minn = (divmod(i, 1))[1]
print(round(maxx - minn, 2))