# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определить
# параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class ItWarehouse:
    def __init__(self, name, series):
        self.name = name
        self.series = series

class OfficeEquipment:
    def __init__(self, name, series):
        self.name = name
        self.series = series

    def __str__(self, name):
        return self.name

class Printer(OfficeEquipment):
    def __init__(self, name, series):
        OfficeEquipment.__init__(self, name, series)


class Scanner(OfficeEquipment):
    def __init__(self, name, series):
        OfficeEquipment.__init__(self, name, series)

class Copier(OfficeEquipment):
    def __init__(self, name, series):
        OfficeEquipment.__init__(self, name, series)

a = Printer('Samsung', 234098)
b = Scanner('Epson', 543789)
c = Copier('Xerox', 567895)

print(a.name, a.series)
print(b.name, b.series)
print(c.name, c.series)

