"""
Упражнение 64. Таблица со скидками
В магазине была объявлена скидка размером 60 % на ряд товаров, и для
того чтобы покупатели лучше ориентировались, владелец торговой точки
решил вывесить отдельную таблицу со скидками с указанием уцененных
товаров и их оригинальных цен. Используйте цикл для создания подобной
таблицы, в которой будут исходные цены, суммы скидок и новые цены для
покупок на сумму $4,95, $9,95, $14,95, $19,95 и $24,95. Убедитесь в том,
что суммы скидки и новые цены отображаются с двумя знаками после
запятой.
"""

disc_rate = 0.6

for price in range(4, 25, 5):
    price += 0.95
    discount = price * disc_rate
    print(f'Исходная цена - {f"${price:.2f}":>6}, скидка - {f"${discount:.2f}":>6}, '
          f'новая цена - {f"${price - discount:.2f}":>6}')