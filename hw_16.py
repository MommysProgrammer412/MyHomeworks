import math
# задача 1
input_seconds = int(input('Введите количество секунд: '))
print(f'{input_seconds // 3600 } час(-а,-ов)', f'{input_seconds % 3600 // 60} минут(-а,-ы)', f'{input_seconds % 3600 % 60} секунда(-а,-ы)', sep='\n')

# задача 2
input_temp = int(input('Введите температуру в градусах цельсия: '))
print(f'Кельвин:{round(input_temp + 273.15, 2)} K', f'Фаренгейт:{round((input_temp * 9/5) + 32, 2)} F', f'Реомюр:{round(input_temp * 4/5, 2)} Ré', sep='\n')