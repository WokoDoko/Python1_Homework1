# Первое задание
duration = int(input('Input time period in SEC.'))

if duration < 60:
    print(duration) # получаем секунды
elif 60 <= duration < 3600:
    print('Введенное количество секунд: {minutes} минут, {seconds} секунд.'.format(minutes = duration//60,seconds = duration%60)) #получаем минуты и секунды
elif 3600 <= duration < 86400:
    print('Введенное количество секунд: {hours} часов, {minutes} минут, {seconds} секунд.'.format(hours=duration//3600, minutes=(duration % 3600) // 60, seconds=(duration % 3600) % 60)) #получаем часы, мин, сек
else:
    print('Введенное количество секунд: {days} суток, {hours} часов, {minutes} минут, {seconds} секунд.'.format(days=duration // 86400, hours=(duration % 86400)//3600, minutes=((duration % 86400) % 3600) // 60, seconds=((duration % 86400) % 3600) % 60)) #получаем дни, часы, минуты и секунды

# Третье задание

number = 1
while number <= 100:
    if number == 1 or number == 21 or number == 31 or number == 41 or number == 51 or number == 61 or number == 71 or number == 81 or number == 91:
        print(str(number) + ' процент')
        number += 1
    elif (number >= 2 and number <= 4) or (number >= 22 and number <= 24) or (number >= 32 and number <= 34) or (number >= 42 and number <= 44) or (number >= 52 and number <= 54) or (number >= 62 and number <= 64) or (number >= 72 and number <= 74) or (number >= 82 and number <= 84) or (number >= 92 and number <= 94):
        print(str(number) + ' процента')
        number += 1
    elif (number >=5 and number <= 20) or (number >= 25 and number <= 30) or (number >= 35 and number <= 40) or (number >= 45 and number <= 50) or (number >= 55 and number <= 60) or (number >= 65 and number <= 70) or (number >= 75 and number <= 80) or (number >= 85 and number <= 90) or (number >= 95 or number == 100):
        print(str(number) + ' процентов')
        number += 1
