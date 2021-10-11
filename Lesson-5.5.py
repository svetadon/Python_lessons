# Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

with open("task_5.txt", "w") as my_file:
    line = input("введите числа через пробел \n")
    my_file.writelines(line)


with open("task_5.txt", "r") as my_file:
    data = my_file.readlines()
    my_file.seek(0)
    print(sum(map(int, my_file.readline().split())))