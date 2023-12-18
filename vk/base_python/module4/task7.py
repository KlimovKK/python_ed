import collections
import datetime
from collections import Counter
from typing import List


def most_common_months(dates: List[str], n) -> List[int]:
    months = []
    for date in dates:
        date_p = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S')
        months.append(int(datetime.datetime.strftime(date_p, '%m')))
    counter = collections.Counter(months)
    common_months = [el[0] for el in counter.most_common(n)]
    return common_months


# code = []
# while data := input():
#     code.append(data)
# code = "\n".join(code)
# exec(code)
