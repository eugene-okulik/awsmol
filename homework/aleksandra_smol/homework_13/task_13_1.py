import os.path
import re
from _datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
my_homework_path = os.path.dirname(base_path)
homework_path = os.path.dirname((os.path.dirname(base_path)))
eugene_homework_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file():
    with open(eugene_homework_path) as eugene_file:
        for lines in eugene_file.readlines():
            yield lines


find_date = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+'

dates = []

for lines in read_file():
    only_date = re.search(find_date, lines).group()
    date_object = datetime.strptime(only_date, '%Y-%m-%d %H:%M:%S.%f')
    dates.append(date_object)

date_1 = dates[0] + timedelta(weeks=1)
print(date_1)

date_2 = dates[1]
print(date_2.strftime('%A'))

date_3 = datetime.now() - dates[2]
print(date_3.days)
