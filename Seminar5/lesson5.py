# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# print('she' == 'She')
# print(ord('S'))
# print(ord('s'))
# # НоУтБуК = 12
# answer = 'HelLLLLOOOooOO, WoRlDDdd!'.lower()
# ans = 'HelLLLLOOOooOO, WoRlDDdd!'.upper()
# print(answer, ans)
# str.lower()
# print('hel' in 'hello')
# Task 20
# word = input("Input word: ").upper()
# data = {'A, E, I, O, U, L, N, S, T, RА, В, Е, И, Н, О, Р, С, Т': 1,
#         'D, GД, К, Л, М, П, У': 2,
#         'B, C, M, P, Б, Г, Ё, Ь, Я': 3,
#         'F, H, V, W, YЙ, Ы': 4,
#         'KЖ, З, Х, Ц, Ч': 5,
#         'J, X, Ш, Э, Ю': 8,
#         'Q, Z, Ф, Щ, Ъ': 10}
# result = 0
# for char in word:
#     for key in data:  # data.keys()
#         if char in key:
#             result += data[key]
# print(result)

# print(*[chr(i) for i in range(1, 1000)])
# print(ord('.'))


# Task 31
# def fib(n):
#     if n in (0, 1):  # a0 = 0 a1 = 1
#         return n
#     return fib(n - 1) + fib(n - 2)
#
#
# print(fib(int(input("Введите номер числа Фибоначчи: "))))
# 0 1 1 2 3
# 0 1 2 3 4
#                    fib(4) ->  fib(3) + fib(2) = 3
#                                |            |
#                        fib(2) + fib(1)    fib(1) + fib(0)
#                         |         |          |        |
#                fib(1) + fib(0)    1          1        0
#                  |         |
#                  1         0
# O(2**n)
# O(2**10) = O(1024)
# n = int(input("Введите номер числа Фибоначчи: "))
# a0, a1 = 0, 1
# for i in range(n):
#     a_next = a0 + a1
#     a0 = a1
#     a1 = a_next
# print(a0)
# # O(n)


# Task 33
# new_list = [i for i in range(5)]
# print(new_list)
# new_list.clear()  # new_list = []
# for i in range(5):
#     new_list.append(i)
# print(new_list)
# n = int(input("Input count marks: "))
# marks = [int(i) for i in input("Input marks: ").split()[:n]]
# print([min(marks) if i == max(marks) else i for i in marks])


# Task 35

# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return (n != 1) * True
#
#
# print('yes' if is_prime(int(input("Input number: "))) else 'no')


# Task 37
# def rec(n):
#     if n == 0:
#         return ''
#     x = int(input("Введите число: "))
#     return rec(n - 1) + f' {x}'


# n = int(input("Введите кол-во чисел: "))
# print(rec(n))
# rec(2) -> x = 3 -> rec(1) + ' 3' = " 4" + " 3"
#                      |
#                    rec(0) + ' 4' = '' + " 4"
#                      |
#                      ''