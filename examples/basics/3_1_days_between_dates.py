# 计算两个日期之间的天数差
from datetime import datetime

def days_between_dates(date1, date2):
    date_format = "%Y-%m-%d"
    delta = datetime.strptime(date2, date_format) - datetime.strptime(date1, date_format)
    return delta.days

date1 = "2023-10-01"
date2 = "2023-10-15"
print(f"Days between {date1} and {date2}: {days_between_dates(date1, date2)}")
