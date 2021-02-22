def parent():
    print("Печать из функции parent ()")

    def first_child():
        print("Печать из функции parent ()")

    def second_child():
        print("Печать из функции second_child ()")

    second_child()
    first_child()


parent()
