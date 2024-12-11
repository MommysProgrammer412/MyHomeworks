from cities import cities_list

cities_set = set()

for city in cities_list:
    cities_set.add(city['name'].lower())

last_letter = ''
last_player = 'компьютер'

while cities_set:
    user_input = input('Введите название города: ').lower()
    if user_input == 'стоп':
        print('Вы завершили игру')
        break
    if last_letter and user_input[0] != last_letter:
        print(f'Вы ввели город на неправильную букву. Нужно было на "{last_letter.upper()}". Вы проиграли.')
        last_player = 'компьютер'
        break
    if user_input not in cities_set:
        print('Такого города нет в списке. Вы проиграли.')
        last_player = 'компьютер'
        break
    print(f'{user_input} - это город из списка')
    cities_set.remove(user_input)
    last_letter = user_input[-1].lower()
    if last_letter in 'ьъ':
        last_letter = user_input[-2].lower()
    last_player = 'игрок'
    matching_cities = {city for city in cities_set if city.startswith(last_letter)}
    
    if matching_cities:
        next_city = matching_cities.pop()
        print(f"Ответ компьютера: {next_city}")
        cities_set.remove(next_city)
        last_letter = next_city[-1].lower()
        if last_letter in 'ьъ':
            last_letter = next_city[-2].lower()
        last_player = 'компьютер'
    else:
        print("У компьютера закончились варианты ответа. Вы победили.")
        break

if not cities_set:
    print("Все города использованы. Игра завершена.")

if last_player == 'игрок':
    print("Поздравляем! Вы победили в игре!")
elif last_player == 'компьютер':
    print("Компьютер победил в игре. Попробуйте еще раз!")