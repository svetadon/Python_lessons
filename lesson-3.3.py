# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    a = int(input('Введите значение а: '))
    b = int(input('Введите значение b: '))
    c = int(input('Введите значение c: '))
    if a > c and b > c:
        return a + b
    elif a > b and c > b:
        return  a + c
    else:
        return a + b

print(my_func(a=(), b=(), c=()))

