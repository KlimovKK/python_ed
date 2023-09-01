"""
Упражнение 57. Счет за телефон
Тарифный план мобильной связи включает в себя 50 минут разговоров
и 50 смс-сообщений за $15,00 в месяц. Каждая дополнительная минута
стоит $0,25, а каждое дополнительное сообщение – $0,15. Все счета за
телефон включают налог на поддержку кол-центров 911 в размере $0,44,
и общая сумма, включающая сумму отчислений кол-центрам, облагается
налогом в размере 5 %.
Напишите программу, которая будет запрашивать у пользователя ко-
личество израсходованных за месяц минут разговора и смс-сообщений
и отображать базовую сумму тарификации, сумму за дополнительные мину-
ты и сообщения, сумму отчислений кол-центрам 911, налог, а также итого-
вую сумму к оплате. При этом дополнительные звонки и сообщения необхо-
димо выводить на экран только в случае их расходования. Убедитесь в том,
что все суммы отображаются в формате с двумя знаками после запятой.
"""

MIN_LIM = 50
SMS_LIM = 50
BASE_TARIFF = 15.00
MIN_PRICE = 0.25
SMS_PRICE = 0.15
TAX911 = 0.44
TAX = 0.05

tax_sum = (BASE_TARIFF + TAX911) * TAX

minutes = int(input('Сколько минут израсходовано за месяц? '))
sms = int(input('Сколько sms израсходовано за месяц? '))

print(f'Базовый тариф: ${BASE_TARIFF}')

if minutes > MIN_LIM:
    min_sum = (minutes - MIN_LIM) * MIN_PRICE
    tax_sum += min_sum * TAX
    print(f'Плата за дополнительные минуты: ${min_sum}')

if sms > SMS_LIM:
    sms_sum = (sms - SMS_LIM) * SMS_PRICE
    tax_sum += sms_sum * TAX
    print(f'Плата за дополнительные sms: ${sms_sum}')

print(f'Сумма отчислений кол-центрам 911 ${TAX911}')
print(f'Сумма налога: ${tax_sum:.2f}')
print(f'Итого к оплате: ${BASE_TARIFF + TAX911 + min_sum + sms_sum:.2f}')
