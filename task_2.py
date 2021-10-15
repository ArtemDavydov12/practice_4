print("Введите ряд чисел: ")
a = int(input())
s = 0
while a >= 0:
    s += a
    a = int(input())
print("Сумма =", s)
