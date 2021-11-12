"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*nums):
    a = []
    for n in nums:
        a.append(n**2)
    return a


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(list_num, arg=None):
    if arg == EVEN:
        return [x for x in list_num if x%2==0]
    if arg == ODD:
        return [x for x in list_num if x%2!=0]
    if arg == PRIME:
        a = []
        for i in list_num:
            if i != 1:
                d = 2
                while i % d != 0:
                    d += 1
                if d == i:
                    a.append(i)
            # else:
            #     a.append(i)
        return a


# print(filter_numbers([1, 2], PRIME))