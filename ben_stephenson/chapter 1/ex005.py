"""
Упражнение 5. Сдаем бутылки
Во многих странах в стоимость стеклотары закладывается определенный
депозит, чтобы стимулировать покупателей напитков сдавать пустые бу-
тылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутыл-
ки большего объема – $0,25.
Напишите программу, запрашивающую у пользователя количество бу-
тылок каждого размера. На экране должна отобразиться сумма, которую
можно выручить, если сдать всю имеющуюся посуду. Отформатируйте
вывод так, чтобы сумма включала два знака после запятой и дополнялась
слева символом доллара.
"""
price_for_less_liter = 0.10
price_for_more_liter = 0.25

less_liter = int(input('Введите количество бутылок объемом 1 литр и меньше: '))
more_liter = int(input('Введите количество бутылок объемом больше 1 литра: '))
sum_all = (less_liter * price_for_less_liter) + (more_liter * price_for_more_liter)
print('Сумма за всю посуду - $%.2f' % sum_all)