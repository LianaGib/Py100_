# TODO Напишите функцию find_common_participants
from time import time

def find_common_participants(first_group: str, second_group: str, sep=","):
    first_group = first_group.split(sep=sep)
    second_group = second_group.split(sep=sep)
    union_group = []
    for name in first_group:
        if name in second_group and name not in union_group:
            union_group.append(name)
    union_group.sort()
    #common_group = a.join(union_group)
    return union_group

def find_common_participants1(first_group: str, second_group: str, sep=","):
    first_group = set(first_group.split(sep=sep))
    second_group = set(second_group.split(sep=sep))
    return sorted(list(first_group.intersection(second_group)))

participants_first_group = "Иванов|Петров|Сидоров|"*10000
participants_second_group = "Петров|Сидоров|Смирнов|"*10000

# TODO Провеьте работу функции с разделителем отличным от запятой
t1 = time()
print(find_common_participants(participants_first_group[:-1], participants_second_group[:-1], sep="|"))
print(time() - t1)

t1 = time()
print(find_common_participants1(participants_first_group[:-1], participants_second_group[:-1], sep="|"))
print(time() - t1)