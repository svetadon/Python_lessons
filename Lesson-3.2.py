# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year_birth, city, email, phone):
    print(name, surname, year_birth, city, email, phone)

my_func(name='Kate', surname='Mos', year_birth='1990', city='New York',
            email='katemos@gmail.com', phone='89002333111')