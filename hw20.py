small_dict = {
    'Человек-муравей и Оса: Квантомания': 2023,
    'Стражи Галактики. Часть 3': 2023,
    'Капитан Марвел 2': 2023,
    'Дэдпул 3': 2024,
    'Капитан Америка: Дивный новый мир': 2024,
    'Громовержцы': 2024,
    'Блэйд': 2025,
    'Фантастическая четвёрка': 2025,
    'Мстители: Династия Канга': 2026,
    'Мстители: Секретные войны': 2027,
    'Безымянный фильм о Человеке-пауке': None,
    'Безымянный фильм о Шан-Чи': None,
    'Безымянный фильм о Вечных': None,
    'Безымянный фильм о мутантах': None
}

#Задача 1
input_film = input('Введите название фильма: ').lower()
films_by_user = []
for film in small_dict.keys():
    if input_film in film.lower():
        films_by_user.append(film)
print(films_by_user)

# Задача 2

#2.1
for key, value in small_dict.items():
    if isinstance(value, int) and value > 2024:
        print(key, value)
    elif value is None:
        continue

#2.2
some_list_2 = []
for key, value in small_dict.items():
    if isinstance(value, int) and value > 2024:
        some_list_2.append(key)
    elif value is None:
        continue
print(some_list_2)

#2.3
some_dict_2 = {}  # Изменено на пустой словарь
for key, value in small_dict.items():
    if isinstance(value, int) and value > 2024:
        some_dict_2[key] = value
    elif value is None:
        continue
print(some_dict_2)

#2.4
some_list_3 = []
for key, value in small_dict.items():
    if isinstance(value, int) and value > 2024:
        some_list_3.append({key, value})
    elif value is None:
        continue
print(some_list_3)