# n = 5
# print(type(n))
"""
n = "sdasf0"
print(type(n))
"""
# n = "asda\"dsfsf"
# print(n)

# a = 5
# b = 5.234
# c = 'sdfa'

# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a,b,c))

# print("Введите 1ю строку")
# a = input()
# print(a)

# print("Введите первое число: ")
# a = input()
# #print(a)
# b = input("Введите второе число: ")
# #print(b)

# print(a, ' + ', b, ' = ', a+b)

# c = 5.89
# print(c)
# n = int(c)
# print(n)

# c = 1
# c = bool(c)
# print(c)

# print("Введите первое число: ")
# a = int(input())
# b = int(input("Введите второе число: "))


# print(a, ' + ', b, ' = ', a+b)

# a = 5.123423553
# b = 6.678987653
# print(round(a*b, 2))

# iter = 2 # iter = iter + 2
# iter += 3 # iter = iter + 3 
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input('Input name: ')
# if username == 'Masha':
#     print('Ура, это же Masha!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ!')
# else:
#     print('Привет, ', username)

# i = 0
# while i < 5:
#     if i == 3:
#         break
#     i +=1
# else:
#     print('Пожалуй хватит!')
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n yf i hfdty 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делитель числа не может привышать введенное число, дененное на 2
#         print(n)
#         flag = False
#     i += 1

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(0, -5) # ----- ничего не выведет
# r = range(1, 10, -2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# for i in r:
#     print(i)

# a = 'qwerty'
# for i in a:
#     print(i)

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ еще этих МяГкИх французких булочек'
# print(len(text)) # выводит количество символов
# print('еще' in text)
# print(text.lower()) # делает все буквы нижнего регистра
# print(text.upper()) # делает все буквы верхнего регистра
# print(text.replace('еще', 'ВСЕ')) # меняет написанное слово на другое

# text = 'съешь еще этих мягких французких булочек'
# print(text[0])  # вывод буквы с
# print(text[1])  # вывод буквы ъ
# print(text[len(text-1)])  # выведет последнюю букву к
# print(text[-5])  # выведет 5 букву с конца л
# print(text[:])  # выведет все предложение
# print(text[:2])  # выведет с начала и до 2 символа
# print(text[10:])  # выведет с 10го символа и до конца
# print(text[len(text)-2:])  # выведет последние буквы ек
# print(text[2:9])  # выведет символы со 2го по 9го
# print(text[6:-18]) # выведет символы с 6го с начала и до 18го с конца
# print(text[0:len(text):6])  # выводит символы с нуля до конца с шагом 6
# print(text[::6])  # выводит символы с нуля до конца с шагом 6

# text = text[2:9] + text[-5] + text[:2]  # выводит символы со 2го по 9й, затем пятый символ с конца и от начала до 2го символа
# print(text)

