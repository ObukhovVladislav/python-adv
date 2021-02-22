# def my_decorator(func):
#     def wrapper():
#         print("Что-то происходит до вызова функции.")
#         func()
#         print("Что-то происходит после вызова функции.")
#
#     return wrapper
#
#
# def say_whee():
#     print("Уи!")
#
#
# say_whee = my_decorator(say_whee)
#
# say_whee()
# say_whee = my_decorator(say_whee)
# # print(say_whee)


from datetime import datetime


def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep

    return wrapper


def say_whee():
    print("Whee!")


say_whee = not_during_the_night(say_whee)
# say_whee()