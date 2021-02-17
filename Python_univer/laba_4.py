n = 70
print("*" * n)
print("Лабораторна робота №4 - Масиви")
print("Студента групи ОФ-01")
print("Павленка Максима")
print("-" * n)
print("""
В заданому користувачем масиві цілих чисел замінити кожний елемент, 
розташований на парній позиції, його факторіалом, 
а розташований на непарній – факторіалом його порядкового індексу.
Знайти середнє арифметичне всіх елементів. 
Відсортувати одержаний  масив за умовою зменшення його елементів. 
Надрукувати вхідний, кінцевий масиви і знайдене середнє арифметичне.
""")
print("*" * n)


def factorial(n):
    if n == 0:
        return 1
    elif n == 0:
        return 1
    return n * factorial(n - 1)


arr = []
temp = ""

while True:
    print("Введіть значення масиву")
    print("Для закінчення нажміть q\n\n")
    while True:
        temp = input()
        if temp == "q":
            break
        elif temp.isdigit():
            arr.append(int(temp))
        else:
            print("Ви ввели щось не те\n")

    print("\n")
    print("Початковий масив:", end=" ")
    print(arr)
    print("\n")

    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = factorial(arr[i])
        else:
            arr[i] = factorial(i)

    print("\n")
    print("Масив після циклу", end=" ")
    print(arr)
    print("\n")
    arr.sort(reverse=True)
    print("Масив після сортування", end=" ")
    print(arr)
    arr = []
    temp = ""
    print("Для виходу з программи натисніть q, або будь який інший символ в разі продовження")
    temp = input()
    if temp == "q":
        break
