numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
average_value = sum([x for x in numbers if x != None])/len(numbers)
for x in range(len(numbers)):
    if numbers[x] == None:
        numbers[x] = average_value
print("Измененный список:", numbers)
