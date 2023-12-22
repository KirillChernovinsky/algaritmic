



################################
##THE INPUT BLOCK
################################
elements = []
main_maze = []



while True:
    user_input = input("Введите 5 числе, которые равны либо 0 либо 1 (когда поле готово введите 'q'): ")
    elements = user_input.split()

    if not user_input == 'q':
        if len(elements) != 5:
            print("должно быть ровно 5 чисел")
        else:
            valid_elements = {"0", "1"}
            if not all(num in valid_elements for num in elements):
                print("Число должно быть либо 1 либо 0")
            else:
                elements = [int(num) for num in elements]
                main_maze.append(elements)
                for el in main_maze:
                    print("Список: ", el)
    else:
        x_coordinate_start = int(input("Введите начальную координату x: "))
        y_coordinate_start = int(input("Введите начальную координату y: "))
        x_coordinate_end = int(input("Введите конечную координату x: "))
        y_coordinate_end = int(input("Введите конечную координату y: "))
        if not x_coordinate_start >= 0 and y_coordinate_start >= 0 and x_coordinate_end >= 0 and y_coordinate_end >= 0:
            print("значения должны быть больше нуля")

        else:

            #определение координат
            start_spisok = main_maze[x_coordinate_start]
            start_element_in_spisok = start_spisok[y_coordinate_start]
            end_spisok = main_maze[x_coordinate_end]
            end_element_in_spisok = end_spisok[y_coordinate_end]
            if start_element_in_spisok == 1 or end_element_in_spisok == 1:
                print('Ничего не выйдет. Координаты ведут в припятствие')



            #перебираем все значения в main_maze и создаем формат вывода
            def schema(main_maze):
                for i in main_maze:
                    for j in i:
                        print('{: 3}'.format(j), end='')
                    print()
                print('----')


            start_coordinate = [(x_coordinate_start, y_coordinate_start)]
            move = 1

            while True:
                schema(main_maze)
                new_coordinate = []
                for x, y in start_coordinate:
                    main_maze[x][y] = move
                    # u
                    if x - 1 >= 0 and main_maze[x - 1][y] == 0:
                        new_coordinate.append((x - 1, y))
                    # d
                    if x + 1 < len(main_maze) and main_maze[x + 1][y] == 0:
                        new_coordinate.append((x + 1, y))
                    # r
                    if y + 1 < 5 and main_maze[x][y + 1] == 0:
                        new_coordinate.append((x, y + 1))
                    # l
                    if y - 1 >= 0 and main_maze[x][y - 1] == 0:
                        new_coordinate.append((x, y - 1))
                start_coordinate = new_coordinate
                move += 1
                if main_maze[x_coordinate_end][y_coordinate_end] != 0:
                    print('ok')
                    break
                print(start_coordinate)
                if not start_coordinate:
                    print('fail')
                    break
            schema(main_maze)
            print(main_maze[-1][-1] - 1)

