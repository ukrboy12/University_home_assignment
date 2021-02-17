n = 70
print("*" * n)
print("Лабораторна робота №5 - Масиви")
print("Студента групи ОФ-01")
print("Павленка Максима")
print("-" * n)
print("""
Вести матрицю. Знайти суму елементів кожного стовпчика. 
Переставити стовпчики матриці у порядку зростання сум елементів у стовпчиках.
""")
print("*" * n)


def inputNumber():
    while True:
        temp = input()
        if temp.isdigit():
            n = int(temp)
            return n
        else:
            print("Ви ввели щось не те")

def sumST(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum


print("Введіть кількість рядків: ")
n = inputNumber()
print("Введіть кількість стовпців: ")
m = inputNumber()
arr = []
tempArr = []
for i in range(n):
    arr.append([])
    for j in range(m):
        arr[i].append(inputNumber())
    print("Новий рядок")
sum = 0
tempSum = 0

for i in range(m):
    for j in range(n):
        print(arr[i][j], end="\t")
    print("\n")

temp = 0
finalArr = []

arr = [*zip(*arr)]
for i in range(m):
    for j in range(m-i-1):
        if sumST(arr[j]) > sumST(arr[j+1]):
            tempArr = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp

arr = [*zip(*arr)]
for i in range(m):
    for j in range(n):
        print(arr[i][j], end="\t")
    print("\n")