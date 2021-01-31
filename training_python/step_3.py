import timeit

name = 'иван'
alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
alphabet.add('ё')


def measure():
    import timeit
    to_measure_1 = '''
    name = 'иван'
    alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
    alphabet.add('ё')
    is_valid = not set(name) - alphabet
    # print(is_valid)
    '''

    to_measure_2 = '''
    name = 'иван'
    alphabet = {chr(el) for el in range(ord('а'), ord('я') + 1)}
    alphabet.add('ё')
    is_valid = True
    for letter in name:
    if letter not in alphabet:
        is_valid = False
        break
    # print(is_valid)
    '''
    print(timeit.timeit(to_measure_1, number=100000))
    print(timeit.timeit(to_measure_2, number=100000))
