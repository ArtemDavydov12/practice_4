c = int(input("Введите стартовоек кол-во: "))
per = int(input("Введите среднесуточное увелечение (в %): "))
days = int(input("введите кол-во дней: "))

k = 0

per = 1 + (per / 100)
print("День    Популяция")
for i in range(days):
    k += 1
    print(k, "     ", round(c, 5))
    c = c * per
