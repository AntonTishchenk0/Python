# HomeTask 24
# n = int(input("Введите кол-во кустов: "))
# count = [int(i) for i in input("Введите через пробел кол-во ягод на "
#                                "каждом кусте: ").split()[:n]]
# print(max([count[i - 2] + count[i - 1] + count[i] for i in range(n)]))


# Task 39
# n = int(input("Введите кол-во элементов 1-ого списка: "))
# first_list = [int(i) for i in input("Введите значения 1-ого списка: ").split()[:n]]
# m = int(input("Введите кол-во элементов 2-ого списка: "))
# second_list = [int(i) for i in input("Введите значения 2-ого списка: ").split()[:m]]
# print(*[i for i in first_list if i not in second_list])


# Task 41
# n = int(input("Введите кол-во элементов списка: "))
# first_list = [int(i) for i in input("Введите значения списка: ").split()[:n]]
# # print(first_list)
# # 12 35 8 9 1
# print(sum([first_list[i - 1] < first_list[i] > first_list[i + 1]
#            for i in range(1, n - 1)]))


# Task 43
# numbers = [int(i) for i in input("Введите числа: ").split()]
# count_numbers = {}
# for i in numbers:
#     if i not in count_numbers:  # count_numbers.keys()
#         count_numbers[i] = 1  # 1 - потому что одно число уже нам встретилось
#     else:  # i является ключом словаря
#         count_numbers[i] += 1
# print(count_numbers)
# print(sum([i // 2 for i in count_numbers.values()]))


# Task 45
# n = int(input("Input number: "))
# data = {}
# for i in range(2, n + 1):
#     summa = 1
#     for j in range(2, i // 2 + 1):  # [2; i // 2] 18 -> [2; 9]
#         if i % j == 0:
#             summa += j
#     data[i] = summa
# print_list = list()
# for k, v in data.items():
#     if v in data.keys() and k in data.values() and k != v and data[v] == k and data[k] == v\
#             and (k, v) not in print_list:
#         print(k, v)
#         print_list.append((v, k))
    
