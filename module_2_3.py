# исправленный вариант

my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while len(my_list) > a:
    if my_list[a] > 0:
        print(my_list[a])
        a += 1
        continue
    elif my_list[a] == 0:
        a += 1
        continue
    elif my_list[a] < 0:
        a += 1
        continue
    else:
        break

# старый вариант, с недочётами.

my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
a = 0
while len(my_list) > a:
    if my_list[a] > 0:
        print(my_list[a])
        a += 1
        continue
    elif my_list[a] >= 0: # если вместо числа ставлю переменную "a", то она уже не равна нулю и до 99 цикл не доходит, значение переменной изменилось.
        # Но почему, если данное условие поставить первым, начинает выходить "69, 13, 99" - я так и не понял.
        a += 1
    else:
        break