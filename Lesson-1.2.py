# 2 задание перевести секунты в часы минуты и секунды


seconds = int(input('Введите время в секундах: '))
hours = seconds // 3600
minutes = (seconds - hours * 3600) // 60
seconds_final = seconds - hours * 3600 - minutes * 60


# перевод в часы
if seconds < 3600:
    print('чч:', 0, 'мм:', minutes, 'сс:', seconds_final)
else:
    if seconds >= 3600:
        print('чч:', hours, 'мм:', minutes, 'сс:', seconds_final)
