list_ = [3, 4, 8, 9, 6, 6, 2, 4, 3, 3, 1]
n = 0 # четные числа
b = 0 # нечетные числа
# TODO завести отдельные счетчики для четных и нечетных чисел

# TODO с помощью одного цикла перебрать все числа и посчитать количество четных и нечетных

# TODO вывести каких чисел больше
for i in list_:
    if i % 2 == 0:
        n += 1
    else: b += 1

if n > b:
    print('Четных чисел больше')
elif n < b:
    print('Нечетных чисел больше')
else:
    print('Четных и нечетных одинаковое количество')

