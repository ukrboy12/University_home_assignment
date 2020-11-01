import math
#todo сделать все проверки
print("Hello")
A = 4
B = 3
C = int(input())
D = int(input())
if D == 0:
    print("Помилка, ділення на нуль")
elif B <=0:
    print("Число B дорівнює нулю, або менше нуля")
else:
    y = (math.cos(A)*math.log1p(B)*C**B)/D
    print("Вивід значення y = ", y)
