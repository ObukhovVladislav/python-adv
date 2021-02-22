# from decorators import do_twice
#
#
# @do_twice
def return_greeting(name):
    print("Создание приветствия")
    return f"Hi {name}"


hi_vlad = return_greeting("Vlad")


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


return_greeting("Vlad")
