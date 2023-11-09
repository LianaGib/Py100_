num = 27  # Число для проверки гипотезы Коллатца
count = 0  # Количество операций над числом




while num > 1:
    if num % 2 == 0:
        num = num/2
        count += 1
    else:
        num = num * 3 + 1
        count += 1
    continue
print("Количество действий:", count)
