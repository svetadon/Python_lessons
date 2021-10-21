# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.
with open("task_2.txt", "r") as my_file:
    data = my_file.read()
    print(f'{data}')

print('количество строк')
with open("task_2.txt", "r") as my_file:
    print(my_file.read().count('\n'))

print('количество слов в строке')
with open("task_2.txt", "r") as my_file:
    data = my_file.read()
    words = data.split()
    print(len(words))