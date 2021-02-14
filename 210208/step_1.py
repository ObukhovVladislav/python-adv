import os
import urllib.parse
import urllib.request

pass
# import cProfile
#
#
# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1
#
#
# def is_palindrome(num):
#     # Skip single-digit inputs
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
#
#
# for i in infinite_sequence():
#     pal = is_palindrome(i)
#     # pal and print(pal)
#     # pal = pal or 'zero'
#     if pal:
#         print(pal)
#
# # cProfile.run('sum([i * 2 for i in range(10000)])')
pass
import re

import requests

RE_XLS_FILE = re.compile(r'href="([^"]+\.xls)"')
RE_PNG_FILE = re.compile(r'href="([^"А-Яа-яЁё]+\.png)"')

# request_url = 'https://kpk.kss45.ru/%D1%83%D1%87%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%B0/%D1%80%D0%B0%D1%81%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5_%D0%BF%D0%B0%D1%80.html'
request_url = 'https://kpk.kss45.ru/учебная-работа/расписание_пар.html'

response = requests.get(request_url)
content = response.content.decode(encoding=response.encoding)

parsed = RE_XLS_FILE.findall(content)
# parsed = RE_PNG_FILE.findall(content)

# f = open('Расписание.txt', 'w', encoding='utf-8')
# for index in parsed:
#     f.write(index + '\n')
#
# # path = "xml/"
# # os.mkdir(path)
# # urllib.request.urlretrieve(request_url, '/users/xml/')
# # urllib.request.urlretrieve(f, 'xml/списание2')
#
# f.close()

pass


def url_encode(request_url):
    protocol, address = request_url.split(':', maxsplit=1)
    return ':'.join([protocol, urllib.parse.quote(address)])


with open('Расписание.txt', 'w', encoding='utf-8') as f:
    path = "xml/"
    if not os.path.isdir(path):
        os.mkdir(path)
    for request_url in parsed:
        urllib.request.urlretrieve(
            url_encode(request_url),
            os.path.join(path, request_url.split('/')[-1])
        )