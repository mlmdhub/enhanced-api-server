from datetime import datetime
import pytz


def timetrans(time_str):
    # 定义时间格式
    time_format = "%a %b %d %H:%M:%S %z %Y"
    time = datetime.strptime(time_str, time_format)

    # 将时间转换为本地时间
    time = time.astimezone(pytz.timezone('Asia/Shanghai'))

    # 输出年月日时分秒
    year = time.year
    month = time.month
    day = time.day
    hour = time.hour
    minute = time.minute
    second = time.second
    return f"{year}-{month}-{day} {hour}:{minute}:{second}"
