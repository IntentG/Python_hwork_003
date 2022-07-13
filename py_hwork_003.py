'''Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:
- 6782 -> 23
- 0,56 -> 11'''

number = input("Введите число, узнаем сумму его цифр:   ")

def CalculateNumbers (number):
    summ = 0
    list = []
    i = 0
    for char in number:
        if char == "." or char == "," or char == "-":
            char = 0
        list.append(int(char))
        summ = summ + list[i]
        i += 1
    return summ

print("\nСумма всех цифр введённого числа: [", CalculateNumbers(number), "]")