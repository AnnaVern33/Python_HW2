# 4 задача. Реализуйте алгоритм перемешивания списка.

import random
list = [1, 34, 23, 54, 7, 9]
random.shuffle(list)

# print(list)

my_list = [1, 2, 3, 7, 98]
length = len(my_list)

for i in range(0, length):
    for j in range(1, length - i):
        my_list[i], my_list[j] = my_list[j], my_list[i]
        i += 1
        j += 1
print(my_list)

