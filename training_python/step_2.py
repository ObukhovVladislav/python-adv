name = 'иван'
# заглавная первая буква, а-я,
# dict
alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')

# set_1 = {'а', 'б', 'в'}
# set_2 = {'а', 'б'}
#
# print(set_1)
# print(set_2 - set_1)
# print(set_1 - set_2)

is_valid = not set(name) - alphabet
print(is_valid)

is_valid = True
for letter in name:
    if letter not in alphabet:
        is_valid = False
        break
print(is_valid)
