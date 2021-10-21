# Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

from datetime import datetime

class Data:

    def __init__(self, str):
        self.str = str
        pass

    def __str__(self):
        return str(self.str)

    @classmethod
    def to_int(cls, str):
        line = datetime.strptime(str, "%d-%m-%Y")
        d = line.day
        m = line.month
        y = line.year
        cls.d = d
        cls.m = m
        cls.y = y
        return d, m, y


    @staticmethod
    def to_valid(param1, param2, param3):
        if (param1 in range(1,31)) and (param2 in range(1,12) and (param3 in range(1900,2100))):
            return True
        else:
            return False



s = input("Введите дату в формате dd-mm-yy: ")
dat = Data(s)

print(dat)
print(dat.to_int(s))
print(dat.d)

x,y, z = dat.to_int(s)
print(dat.to_valid(x,y,z))