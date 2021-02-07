# def is_palindrome(num):
#     if num // 10 == 0:
#         return False
#     temp = num
#     reversed_num = 0
#
#     while temp != 0:
#         reversed_num = (reversed_num * 10) + (temp % 10)
#         temp = temp // 10
#
#     if num == reversed_num:
#         return num
#     else:
#         return False

# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     if pal:
#         print(pal)

# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1

# nums_squared_lc = [num**2 for num in range(5)]
# nums_squared_gc = (num**2 for num in range(5))

# import sys
#
# nums_squared_lc = [i * 2 for i in range(10000)]
# sys.getsizeof(nums_squared_lc)

# nums_squared_gc = (i ** 2 for i in range(10000))
# print(sys.getsizeof(nums_squared_gc))

# import cProfile
#
# cProfile.run('sum([i * 2 for i in range(10000)])')
# cProfile.run('sum((i * 2 for i in range(10000)))')


# def multi_yield():
#     yield_str = "This will print the first string"
#     yield yield_str
#     yield_str = "This will print the second string"
#     yield yield_str
#
#
# multi_obj = multi_yield()
# print(next(multi_obj))
# print(next(multi_obj))


letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)
