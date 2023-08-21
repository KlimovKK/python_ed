"""
Упражнение 11. Потребление топлива
В США потребление автомобильного топлива исчисляется в милях на
галлон (miles-per-gallon – MPG). В то же время в Канаде этот показатель
обычно выражается в литрах на 100 км (liters-per-hundred kilometers –
L/100 km). Используйте свои исследовательские способности, чтобы опре-
делить формулу перевода первых единиц исчисления в последние. После
этого напишите программу, запрашивающую у пользователя показатель
потребления топлива автомобилем в американских единицах и выводя-
щую его на экран в канадских единицах.
"""
mpg = float(input('Введите расход топлива в милях на галлон: '))
lpk = (100 * 3.78541) / (mpg * 1.60934)
print(f'Расход топлива в нормальных единицах - {lpk: .3f} литров на 100 км')
