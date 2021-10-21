# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными. Определить метод расчета массы асфальта,
# необходимого для покрытия всего дорожного полотна. Использовать формулу:
# длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
# толщиной в 1 см * число см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    _length = None
    _width = None
    weight = None
    thickness = None

    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        self.weight = 25
        self.thickness = 5
        mass = self._length * self._width * self.weight * self.thickness / 1000
        print(f'Требуется {mass} тонн асфальта')

Road_result = Road(5000, 20)
Road_result.mass()
