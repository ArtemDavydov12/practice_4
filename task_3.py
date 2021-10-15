c = int(input("Введите число: "))
k = 1
f = 1
for i in range(c):
    f = k * f
    k += 1
print(c, "! = ", f)
