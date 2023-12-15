import datetime

string_datetime = input()


def parse_time(s):
    dt = datetime.datetime.strptime(s, '%Y %m %d %H %M %S')
    delta = datetime.timedelta(days=1)
    dt = dt + delta
    return int(dt.strftime('%d'))


print(parse_time(string_datetime))
