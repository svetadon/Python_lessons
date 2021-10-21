# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
# о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} едет'
    def stop(self):
        return f'{self.name} остановилась'
    def turn(self, direction):
        return f'{self.name} повернула {direction}'
    def show_speed(self):
        return f'со скорость {self.speed}'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 60:
            return f'{self.name} вы превысили скорость'
        else:
            return f'{self.name} ваша скорость в пределах нормы'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'{self.name} едет со скоростью {self.speed}')
        if self.speed > 40:
            return f'{self.name} вы превысили скорость'
        else:
            return f'{self.name} ваша скорость в пределах нормы'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} {self.color} - полицейская машина'
        else:
            return f'{self.name} {self.color} - не полицейская машина'

porsche = SportCar(100, 'красный', 'Porsche', False)
toyota = TownCar(80, 'белый', 'Toyota', False)
gaz = WorkCar(30, 'желтый', 'Gaz', False)
ford = PoliceCar(90, 'синий', 'Ford', True)


print(f'{porsche.turn(direction="налево")}')
print(toyota.show_speed())
print(gaz.show_speed())
print(ford.police())
print(ford.turn(direction="направо"))
print(f'{porsche.go()} {porsche.show_speed()}')



