"""
Напишите программу, которая определяет, будет ли положительное целое число степенью четвёрки.
Подсказка: степенью четвёрки будут все числа вида 4n, где n – целое неотрицательное число.
На вход подаётся целое число в диапазоне от 1 до 10000.
"""
num = int(input())


for i in range(0, 8):
    if 4**i == num:
        print(True)
        break
else:
    print(False)