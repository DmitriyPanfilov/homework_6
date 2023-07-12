# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


my_list = list(map(int, input('Введите элементы массива через пробел: ').split()))
minimum = int(input('Введите минимальное число: '))
mаximum = int(input('Введите максимальное число: '))
resalt = []
for ind, value in enumerate(my_list):
    if minimum <= value <= mаximum:
        resalt.append(ind)
print(* resalt, sep=', ')

