# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

rating = int(input('Введите новый рейтинг: '))
my_list = [7, 5, 3, 3, 2]
i = my_list.count(rating)

for el in my_list:
    if i > 0:
        a = my_list.index(rating)
        my_list.insert(a + i, rating)
        break
    else:
        if rating > el:
            b = my_list.index(el)
            my_list.insert(b, rating)
            break
        elif rating < my_list[len(my_list) - 1]:
            my_list.append(rating)
print(my_list)





