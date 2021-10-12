"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(list_numbers):
    return [x**2 for x in list_numbers]



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(list_num, arg=None):
    if arg == "odd":
        return [x for x in list_num if x%2==0]
    if arg == "even":
        return [x for x in list_num if x%2!=0]
    if arg == "prime":
        a = []
        for i in list_num:
            if i != 1:
                d = 2
                while i % d != 0:
                    d += 1
                if d == i:
                    a.append(i)
            else:
                a.append(i)
        return a
# print(filter_numbers([1,2,3,4,5], "odd"))