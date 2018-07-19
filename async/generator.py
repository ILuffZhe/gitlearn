# -*- coding: utf-8 -*-
# @Time    : 2018/6/23 17:20
# @Author  : ILuffZhe
# @Software: PyCharm


def form_range(max):
    index = 0
    while index < max:
        jump = yield index
        if not jump:
            jump = 1
        index += jump


def main():
    iterator = form_range(5)
    print(next(iterator))  # 0
    print(iterator.send(2))  # 2
    print(next(iterator))  # 3
    print(iterator.send(-1))  # 2
    for x in iterator:
        print(x)  # 3 4


if __name__ == "__main__":
    main()