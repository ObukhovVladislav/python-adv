def my_decorator(func):
    def wrapper():
        print("Что-то происходит до вызова функции.")
        func()
        print("Что-то происходит после вызова функции.")

    return wrapper


@my_decorator
def say_whee():
    print("Whee!")

