


#
# ################################
# ##THE INPUT BLOCK
# ################################
# elements = []
# main_maze = []
#
#
#
# while True:
#     user_input = input("Введите 5 числе, которые равны либо 0 либо 1 (когда поле готово введите 'q'): ")
#     elements = user_input.split()
#
#     if not user_input == 'q':
#         if len(elements) != 5:
#             print("должно быть ровно 5 чисел")
#         else:
#             valid_elements = {"0", "1"}
#             if not all(num in valid_elements for num in elements):
#                 print("Число должно быть либо 1 либо 0")
#             else:
#                 elements = [int(num) for num in elements]
#                 main_maze.append(elements)
#                 for el in main_maze:
#                     print("Список: ", el)
#     else:
#         x_coordinate_start = int(input("Введите начальную координату x: "))
#         y_coordinate_start = int(input("Введите начальную координату y: "))
#         x_coordinate_end = int(input("Введите конечную координату x: "))
#         y_coordinate_end = int(input("Введите конечную координату y: "))
#         if not x_coordinate_start >= 0 and y_coordinate_start >= 0 and x_coordinate_end >= 0 and y_coordinate_end >= 0:
#             print("значения должны быть больше нуля")
#
#         else:
#
#             #определение координат
#             start_spisok = main_maze[x_coordinate_start]
#             start_element_in_spisok = start_spisok[y_coordinate_start]
#             end_spisok = main_maze[x_coordinate_end]
#             end_element_in_spisok = end_spisok[y_coordinate_end]
#             if start_element_in_spisok == 1 or end_element_in_spisok == 1:
#                 print('Ничего не выйдет. Координаты ведут в припятствие')
#
#             elif x_coordinate_start == x_coordinate_end:
#             # начальный x == конечному x , то нужно двигаться только по y
#                 if y_coordinate_start == y_coordinate_end:
#                     print('Начальные координаты совпали с конечными')
#
#                     # начальный x == конечному x , то нужно двигаться только по y тут вправо
#                 elif y_coordinate_start < y_coordinate_end:
#                     for ell in range(y_coordinate_end - y_coordinate_start):
#                         ouk = int(y_coordinate_start) + ell
#                         print(x_coordinate_start, ouk + 1)
#                         if start_spisok[ouk + 1] == 1:
#                             print("Ничего не выйдет")
#                             break
#
#                 # начальный x == конечному x , то нужно двигаться только по y тут влево
#                 elif y_coordinate_start > y_coordinate_end:
#                     for ell in range(y_coordinate_start - y_coordinate_end):
#                         ouk = int(y_coordinate_start) - ell
#                         print(x_coordinate_start, ouk - 1)
#                         if start_spisok[ouk - 1] == 1:
#                             print("не выйдет")
#                             break
#
#
#
#
#
#
#             #начальный y == конечному y , то нужно двигаться только по x
#             elif y_coordinate_start == y_coordinate_end:
#
#                     # начальный y == конечному y , то нужно двигаться только по x тут вниз
#                 if x_coordinate_start < x_coordinate_end:
#                     for ell in range(x_coordinate_end - x_coordinate_start):
#                         ouk = int(x_coordinate_start) + ell
#                         x = main_maze[ouk + 1][y_coordinate_start]
#                         print(f'{ouk + 1};{y_coordinate_start}')
#                         if x == 1:
#                             print("Ничего не выйдет")
#                             break
#
#                     # начальный y == конечному y , то нужно двигаться только по x тут вверх
#                 elif x_coordinate_start > x_coordinate_end:
#                     for ell in range(x_coordinate_start - x_coordinate_end):
#                         ouk = int(x_coordinate_start) - ell
#                         x = main_maze[ouk - 1][y_coordinate_start]
#                         print(f'{ouk - 1};{y_coordinate_start}')
#                         if x == 1:
#                             print("Ничего не выйдет")
#                             break
#             elif 0 < 1:
#                 #определяем есть ли в рядях между координатами x ряды, в которых все значения 1 (берем все ряды между
#                 #изначальных и проверяем их на наличие 1 1 1 1 1
#                 for i in range(x_coordinate_start + 1, x_coordinate_end):
#                     if all(x == 1 for x in main_maze[i]):
#                         print('Ничего не выйдет. Есть ряд со сплошными припятствиями')


#
# x_coordinate_end = 2
# y_coordinate_end = 3
# new_coordinate = [(2, 3)]
#
# v = (x_coordinate_end,y_coordinate_end)
# b = new_coordinate[-1]
# if v == b:
#     print('asdas')


