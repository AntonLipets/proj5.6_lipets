
format = "Формат хода двузначное число. Первая цифра - строка (0-2), вторая цифра столбец (0-2)"
print(format)
xstep = True
table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]
def print_table (table):
    print("  0 1 2")
    k = 0
    for string in table:
        print(k, *string)
        k += 1
while True:
    correct_move = False
    # проверка корректности ввода
    while not correct_move:
        print_table(table)
        print("Ход крестиков") if xstep else print("Ход ноликов")
        move = input()
        if len(move) == 2 and any([move[0]=="0", move[0]=="1", move[0]=="2"]) and any([move[1]=="0", move[1]=="1", move[1]=="2"]):
            correct_move = True
        else:
            print("Не корректный формат хода")
            print(format)

    # изменение поля
    i = int(move[0])
    j = int(move[1])
    if xstep:
        value = "x"
    else:
        value = "o"
    if not table[i][j] == "-":
        print("Там уже занято")
        continue
    table[i][j] = value
    # проверка выигрыша
    # строки
    inline = 0
    for k in range(3):
        if table[i][k] == value:
            inline += 1
        else:
            break
    if inline == 3:
        print_table(table)
        print("Победили крестики") if xstep else print("Победили нолики")
        break
    # строки
    inline = 0
    for k in range(3):
        if table[k][j] == value:
            inline += 1
        else:
            break
    if inline == 3:
        print_table(table)
        print("Победили крестики") if xstep else print("Победили нолики")
        break
    # диаганали
    indiag1 = 0
    indiag2 = 0
    for k in range(3):
        if table[k][k] == value:
            indiag1 += 1
        if table[k][2-k] == value:
            indiag2 += 1
    if indiag1 == 3 or indiag2 ==3:
        print_table(table)
        print("Победили крестики") if xstep else print("Победили нолики")
        break
    # проверка на ничью
    draw = True
    for i in range(3):
        for j in range(3):
            if table[i][j] == "-":
                xstep = not xstep
                draw = False
                break
        if not draw:
            break
    if draw:
        print_table(table)
        print("Ничья")
        break
