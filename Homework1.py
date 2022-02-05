"""
Напишите программу, которая считает общую цену. Вводится M рублей и N копеек
цена, а также количество S товара Посчитайте общую цену в рублях и копейках за
L товаров.
Пример:
Input: Цена одной вещи 3 рубля 20 копеек, посчитать 3 предмета.
Output: Общая цена 9 рублей 60 копеек
Задачу поместите в файл task1.py в папке src/homework1.
"""

rub = int(input('Введите Рубли '))
pound = int(input('Введите копейки '))
quantity = int(input('Введите количество товара '))

result = ((rub * 100) + pound) * quantity
result_rub = result // 100
result_pound = result % 100

print('Общая стоимость составит ' + str(result_rub) + ' рублей ' + str(result_pound) + ' копеек')
