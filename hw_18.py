input_text = input('Введите текст: ')
input_num = int(input('Введите число: '))
special = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
result = ''
for i in input_text:
    if i in special:
        new_ord = ord(i) + input_num
        new_char = chr(new_ord)
        result += new_char
    else:
        result += i
print(result)