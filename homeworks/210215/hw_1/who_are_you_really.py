# print(type(print))
# print(print.__name__)
# help(print)
# print(...)

# print(type(say_whee))
# print(say_whee.__name__)
# help(say_whee)
# wrapper_do_twice()

import functools


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


# say_whee
# say_whee.__name__
# help(say_whee)
# say_whee()
