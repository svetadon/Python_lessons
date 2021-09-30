# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.

el_count = int(input("Введите количество элементов списка "))
my_list = []
i = 0
num = 0
while i < el_count:
    my_list.append(input("Введите значение списка "))
    i += 1

for elem in range(int(len(my_list)/2)):
        my_list[num], my_list[num + 1] = my_list [num + 1], my_list[num]
        num += 2
print(my_list)