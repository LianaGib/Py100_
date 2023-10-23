numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
len_ = (len(numbers))
numbers.remove(None)
average_value = sum(numbers)/len_
for num in numbers:
    if (num == None):
         num = average_value
print("Измененный список:", numbers)
