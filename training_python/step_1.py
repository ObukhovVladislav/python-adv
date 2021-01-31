name = 'иван'
# заглавная первая буква, а-я,
# dict
alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet_2 = [chr(el) for el in range(ord('а'), ord('я') + 1)]
alphabet_3 = {chr(el): el for el in range(ord('а'), ord('я') + 1)}

print(type(alphabet), type(alphabet_2), type(alphabet_3))

# print('d' in alphabet)
# print('d' in alphabet_2)
# print(alphabet)
# print(alphabet_3)
print('z' in alphabet, 'г' in alphabet)  # O(1)
print('z' in alphabet_2, 'г' in alphabet_2)  # (n)
print('z' in alphabet_3, 'г' in alphabet_3)  # O(1)
print(alphabet)
print(alphabet_2)
print(alphabet_3.keys())