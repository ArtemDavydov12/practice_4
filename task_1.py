v = int(input("введите скорость в км/ч:"))
t = int(input("Введите время в часах:"))
c = 0
for i in range(t):
    c += 1
    print(c, "   ", v*c)
