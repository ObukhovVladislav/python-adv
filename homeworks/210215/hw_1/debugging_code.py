# import functools
#
#
# def debug(func):
#     """Распечатайте подпись функции и возвращаемое значение"""
#
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]  # 1
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
#         signature = ", ".join(args_repr + kwargs_repr)  # 3
#         print(f"Вызов {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} вернулся {value!r}")  # 4
#         return value
#
#     return wrapper_debug
#
#
# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Привет {name}!"
#     else:
#         return f"Привет {name}! {age} вы уже растете!"
#
#
# make_greeting("Владислав")
# make_greeting("Владислав", age=18)
# make_greeting(name="Евгений", age=18)


# import math
# from decorators import debug
#
# # Apply a decorator to a standard library function
# math.factorial = debug(math.factorial)
#
#
# def approximate_e(terms=18):
#     return sum(1 / math.factorial(n) for n in range(terms))
#
#
# approximate_e(5)
