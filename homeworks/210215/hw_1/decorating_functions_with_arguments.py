# from decorators import do_twice
#
#
# @do_twice
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#
#
# def greet(name):
#     print(f"Hello {name}")
#
#
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#
#     return wrapper_do_twice
