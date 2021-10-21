# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение
# и считывающую построчно данные. При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

rus = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}


with open("task_4.txt", "r") as my_file:
    for line in my_file:
        eng = line.split()[0]
        rus_new = rus.get(line.split()[0])
        new_file = line.replace(eng, rus_new)
        print(new_file)

with open('task_4_new.txt', 'w') as my_file_2:
    my_file_2.writelines(new_file)