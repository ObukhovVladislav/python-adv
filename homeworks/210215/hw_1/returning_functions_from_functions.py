def parent(num):
    def first_child():
        return "Привет я Владислав"

    def second_child():
        return "Зови меня Влад"

    if num == 1:
        return first_child
    else:
        return second_child


first = parent(1)
second = parent(2)
# print(first)
# print(second)
# print(first())
# print(second())
