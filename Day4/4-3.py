#!/usr/bin/python
# -*- coding: <utf-8> -*-
# treasure map
'''
Write a program that gives the user a 3*3 grid and asks the user to place the treasure in the grid.
Grid Format - [[list1][list2][list3]]
input format - column number.row number
'''


def three():
    list1 = ["-", "-", "-"]
    list2 = ["-", "-", "-"]
    list3 = ["-", "-", "-"]
    s = [list1, list2, list3]

    print(list1)
    print(list2)
    print(list3)

    c = input("Enter column number between 1 and 3 - ")
    r = input("Enter row number between 1 and 3 - ")

    c = int(c)-1
    r = int(r)-1

    s[r][c] = "x"

    print(list1)
    print(list2)
    print(list3)


three()
