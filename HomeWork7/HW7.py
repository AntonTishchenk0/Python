# Task 1:
# Напишите функцию print_operation_table(operation, num_rows, num_columns), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.

# def print_operation_table(operation, num_rows , num_columns ):
#  if num_rows < 2 or num_columns < 2:
#   print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#  else:
#   print(' '.join([str(i) for i in range(1, num_columns + 1)]))
#   for i in range(2, num_rows + 1):
#    print(i, end = ' ')
#    for j in range(2, num_columns + 1):
#     print(operation(i, j), end = ' ')
#    print()


# num_rows = int(input('Введите количество строк: ')) 
# num_columns = int(input('Введите количество колонок: '))
# print_operation_table(lambda x, y: x * y, num_rows, num_columns)

