import datetime

def printCurrentTime():
    current_datetime = datetime.datetime.now()
    print("current time is {}" .format(current_datetime))

def printSpecificTime():
    specific_datetime = datetime.datetime(2023, 6, 25, 9, 35, 0)
    print("specific time is {}" .format(specific_datetime))  # specific time is 2023-06-25 09:35:00
    # 获取年份
    year = specific_datetime.year

    # 获取月份
    month = specific_datetime.month

    # 获取日期
    day = specific_datetime.day

    # 获取小时
    hour = specific_datetime.hour

    # 获取分钟
    minute = specific_datetime.minute

    # 获取秒数
    second = specific_datetime.second

    # 获取微秒数
    microsecond = specific_datetime.microsecond

    print("year is {}" .format(year))
    print("month is {}" .format(month))
    print("day is {}" .format(day))
    print("hour is {}" .format(hour))
    print("minute is {}" .format(minute))
    print("second is {}" .format(second))
    print("microsecond  is {}" .format(microsecond ))

    formatted_datetime = specific_datetime.strftime('%Y-%m-%d %H:%M:%S')
    print("formatted time is {}" .format(formatted_datetime))

    date_string = '2023-06-25'
    parsed_date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    print("parsed date is {}" .format(parsed_date))

def calculateDatetime():
    specific_datetime = datetime.datetime(2023, 6, 30, 0, 35, 0)
    # 增加一天
    next_day = specific_datetime + datetime.timedelta(days=1)

    # 减去一小时
    previous_hour = specific_datetime - datetime.timedelta(hours=1)

    print("next day is {}" .format(next_day))    # next day is 2023-07-01 00:35:00
    print("previous hour is {}" .format(previous_hour))  # previous hour is 2023-06-29 23:35:00

def compareDatetime():
    date1 = datetime.datetime(2023, 6, 25)
    date2 = datetime.datetime(2023, 6, 24)

    if date1 < date2:
        print('date1 is earlier than date2')
    else:
        print('date1 is later than date2')



if __name__=='__main__':
    # printCurrentTime()
    # printSpecificTime()
    # calculateDatetime()
    compareDatetime()


