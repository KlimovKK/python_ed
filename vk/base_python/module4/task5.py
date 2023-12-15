import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    delta = datetime.timedelta(days=days, seconds=seconds)
    dt = datetime.datetime.strptime('01.01.2023 12:30:00', '%d.%m.%Y %H:%M:%S')
    dt = dt + delta
    return int(dt.strftime('%d')), int(dt.strftime('%S'))


print(shift_time(days, seconds))
