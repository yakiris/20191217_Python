# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

print('Преобразователь секунд в чч:мм:сс')
print(50 * '-')
user_second = int(input('Введите количество секунд: '))

hour = user_second // 3600
if 0 <= hour < 9:
    hour = '0' + str(hour)
ost_hour = user_second % 3600
minute = ost_hour // 60
if 0 <= minute < 9:
    minute = '0' + str(minute)
second = ost_hour % 60
if 0 <= second < 9:
    second = '0' + str(second)
print(hour, minute, second, sep=':')
# или
print(f'{user_second} секунд(а) = {hour}:{minute}:{second}')