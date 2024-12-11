input_name = input('Введите имя:')
input_mark = input('Введите оценку:')

initial = 'начальный'
medium = 'средний'
sufficient = 'достаточный'
high = 'высокий'

if input_mark.isdigit():
    new_mark = int(input_mark)
    if 0 < new_mark < 4:
        print(f'Имя студента: {input_name}. Уровень: {initial}') 
    elif 3 < new_mark < 7:
        print(f'Имя студента: {input_name}. Уровень: {medium}')
    elif 6 < new_mark < 10:
        print(f'Имя студента: {input_name}. Уровень: {sufficient}')
    elif 9 < new_mark < 13:
        print(f'Имя студента: {input_name}. Уровень: {high}')
    else:
        print(f'{new_mark} - некорректно введена оценка')
