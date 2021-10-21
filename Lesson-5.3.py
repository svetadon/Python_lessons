# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

salary = []
summa = 0
count = 0
with open("task_3.txt", "r") as my_file:
    for line in my_file:
        name, salary = line.split()
        salary = int(salary)
        if salary <= 20000:
            print(name, salary)
        summa += salary
        count += 1
result = summa / count
print(f'average salary: {result}')