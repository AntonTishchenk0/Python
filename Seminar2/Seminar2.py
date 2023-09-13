# name = "Ivan"
# #       0123
# print(name[0])
# foreach - C#
# for element in "Hello", 123, 34.125, True, 'a':
#     print(element * 2)
# 0: element = "Hello"
# 1: element = 123
# 2: element = 34.125
# ...
# range и for между собой НИКАК НЕ СВЯЗАНЫ!!!
# range(begin=необязательный(0), end=обязательный, step=необязательный(+1))
# print(*range(5))
# # 0 1 2 3 4
# print(*range(5, 0, -1))
# print(*range(5, 13, 2))
# print(*range(2, 10))
# print(*range(0, 8, 2))

# for i in range(5):
#     # print(i, end=' ')
#     print(i, end='!\n')

# print(1, end=', ')
# print(2, end='. ')
# print(3, end='!\n')
# # print()
# print("Hello")

# print("Ivan")


# from numpy import arange

# for i in arange(0.0, 1.23, 0.01):
#     print(i)


# Task 9
# n = int(input("Input number: "))
# result = 1
# while n > 1:
#     result *= n # result = result * n
#     n -= 1
# print(result)
# Task 11

# n = int(input("Введите число: "))
# first_fib = 0
# second_fib = 1
# i = 2 # Первые два числа уже известны
# while second_fib < n:
#     next_fib = first_fib + second_fib
#     # 0 1 1 2 3 5 8
#     # 1 + 1 = 2
#     first_fib = second_fib
#     second_fib = next_fib
#     i += 1
#     if second_fib > n:
#         i = -1
# print(i)


# Task 15
# n = int(input("Введите кол-во арбузов: "))
# x = int(input("Введите массу арбуза: "))
# max_massa = min_massa = x
# for i in range(n - 1): 
#     x = int(input("Введите массу арбуза: "))
#     if max_massa < x:
#         max_massa = x
#     elif min_massa > x: 
#         min_massa = x
# print(min_massa, max_massa)


# Task 13
# n = int(input("Введите кол-во дней: "))
# count = 0
# max_count = 0
# for i in range(n):
#     temp = int(input("Введите температуру: "))
#     if temp > 0:
#         count += 1
#         if max_count < count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)
