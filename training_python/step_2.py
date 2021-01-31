name = 'иван'
# заглавная первая буква, а-я,
# dict
alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}

set_1 = {'а', 'б', 'в'}
set_2 = {'а', 'б'}

print(set_2 - set_1)