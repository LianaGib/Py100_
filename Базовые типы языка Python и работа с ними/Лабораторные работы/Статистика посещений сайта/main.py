users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
users_all = {"Общее количество": 0}
users_unique = {"Уникальные посещения": 0}
users_all["Общее количество"] = len(users)
users_unique["Уникальные посещения"] = len(set(users))
print(users_all | users_unique)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
