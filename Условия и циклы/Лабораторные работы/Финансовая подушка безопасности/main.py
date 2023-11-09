money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month = 10
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
for month in range(2, month+1):
    spend = spend+spend*increase
    #month = month + 1
    print(spend)
while money_capital > 0:
    money_capital = money_capital + salary*month
    money_capital -= spend
    print(money_capital)
    break









print("Количество месяцев, которое можно протянуть без долгов:", )
