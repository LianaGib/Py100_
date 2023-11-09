# TODO Распечатать таблицу умножения
for a in range(2, 10):
    for b in range(2, 10):
        c = a * b
        if c < 10:
            print(f"  {c}", end='')
        else:
            print(f" {c}", end='')
    print()
