# Task 25: 
# Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# str1 = 'a a a b c a a d c d d'
# str1 = str1.split()
# my_dict = {}

# for i in str1:
#     if i not in my_dict:
#         my_dict[i] = 0
#         print(i, end = " ")
#     else:
#         my_dict[i] += 1
#         print(f'{i}_{my_dict[i]}', end=' ')

# Task 27:
# Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним пробелом. Определите, сколько различных слов содержится в этом тексте.

# str1 = '''She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells'''.lower()
# str1 = set(str1.split())
# print(len(str1))

# # or

# print(len(set(input("Input text: ").lower().split())))

