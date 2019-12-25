# -*-coding: utf-8 -*-
def bubble_sort(list1):
    n = len(list1)
    for i in range(0, n - 1):
        for j in range(0, n - 1 - i):
            if list1[j] > list1[j + 1]:
                list1[j], list1[j + 1] = list1[j + 1], list1[j]
    print(list1)


if __name__ == '__main__':
    list1 = [1, 3, 4, 6, 7, 9, 45, 12, 0]
    bubble_sort(list1)
