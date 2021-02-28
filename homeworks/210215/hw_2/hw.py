# def example(name):
#     word = 'Привет'
#     return f"Слово: {word}, 'Длина строки этого слова", len(word)
#
#
# def passable_function(greeter_func):
#     return greeter_func('')
#
#
# print(passable_function(example))


def my_decorator(func):
    def text_len(str_len):
        print(f"Длина строки = {len(str_len)} символов")
        return func(str_len)
        # print(str_len)
        # return f"Длина строки = {func(len(str_len))} символов"

    return text_len


@my_decorator
def me_function_text(text_str):
    return text_str


sample_1 = 'Вроде так должно получится'
sample_1 = me_function_text(sample_1)
print(sample_1)

# sample_2 = 'Но это не точно'
# sample_2 = me_function_text(sample_2)
# print(sample_2)
