import math


# for i in range(10000, 99999):
#     x1 = int(i / 10000)
#     x2 = int((i - x1 * 10000) / 1000)
#     x3 = int((i - x1 * 10000 - x2 * 1000) / 100)
#     x4 = int((i - x1 * 10000 - x2 * 1000 - x3 * 100) / 10)
#     x5 = i - x1 * 10000 - x2 * 1000 - x3 * 100 - x4 * 10
#     a1 = x1
#     b1 = x2 * 10 + x3
#     c1 = x4 * 10 + x5
#     a2 = x1 * 10 + x2
#     b2 = x3 * 10 + x4
#     c2 = x5
#     if 2 * b1 == a1 + c1:
#         print(i)
#     elif 2 * b2 == a2 + c2:
#         print(i)


def xy(x: object, y: object) -> object:
    res = (x + y) / (x * y + 4)
    return (res)


a = 2015
for i in range(2015, 0, -1):
    a = xy(a, i - 1)
    print(i, a)
