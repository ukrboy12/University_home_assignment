from math import *
from msvcrt import getch
print(""" 
    1. підрахувати значення функції y за варіантом
    2. вивести на екран результат обчислення функції y = b^3   , якщо в >0, або функції  в інших випадках.
    3. вивести за абеткою слова “first” та слово с, вказане користувачем.
    4. вивести на екран код клавіши натиснутої користувачем.""")

option = int(input("Введіть цифру одного з варіантів з варіантів: "))
if option == 1: 
    a = int(input("Введіть значення a: "))
    if a<=0:
        result = cos(a)*(sin(a)**2)
        print("Результат: ", result)
    elif a == 1: 
        result = cos(a)
        print("Результат: ", result)
    else: 
        result = a**3-5*(a**2)+12
        print("Результат: ", result)
elif option == 2:
    b = int(input("Введіть значення b: "))
    if b>0:
        result = b**3
        print("Результат: ", result)
    else:
        result = 2*b**3-b
        print("Результат: ", result)
if option==3:
    word = input("Введіть слово англійською мовою: ")
    if "first"<word.lower():
        print("first"+" "+word)
    else:
        print(word+" "+"first")
if option == 4:
    key = ord(getch())
    print(key)