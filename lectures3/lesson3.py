# Task 1:

# 1:

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     print(summa)

# sum_numbers(5)

# 2:

# def sum_numbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# 3:

# def sum_numbers(n, y = "Hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5))

# 4:

# def sum_numbers(n, y = "Hello"):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sum_numbers(5, "qwerty"))

# Task 2:

# *args - можем передать неограниченное количество аргументов.

# def sum_str(*args):
#     res = ""
#     for i in args:
#         res += i
#     return res

# print(sum_str('q', 'w', 'e', 'r', 't', 'y'))

# Task 3:

# 1:

# import modul1

# print(modul1.max1(5, 9))

# 2:

# from modul1 import max1

# print(max1(11, 9))

# 3:

# from modul1 import *

# print(max1(11, 9))

# 4:

# import modul1 as m1

# print(m1.max1(11, 8))

# Task 4:

# def fib(n):
#     if n in [1,2 ]:
#         return 1
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Task 5:

# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([14, 5, 9, 1, 24, 45, 2, 6]))

# Task 6:

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list1 = [1, 2, 5, 67, 5, 2, 6, 7, 9]
# merge_sort(list1)
# print(list1)
