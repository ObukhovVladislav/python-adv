def do_twice(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice

#
# from decorators import do_twice
#
#
# @do_twice
# def say_whee():
#     print("Уи!")
