# Список словарей со студентами и их оценками
students = [
    {"name": "Маша", "grade": 4},
    {"name": "Петя", "grade": 3},
    {"name": "Саша", "grade": 5},
    {"name": "Кирилл", "grade": 2},
    {"name": "Оля", "grade": 4},
]

# TODO Распечатать имена студентов с оценками выше тройки
for name in students:
    if name['grade'] > 3:
        print(name["name"] +".", "Оценка:", name["grade"])


