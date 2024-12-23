from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

def split_into_monthly_ranges(start_date, end_date):
    # 确保输入日期为 datetime 对象
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # 初始化结果列表
    date_ranges = []

    # 当前开始日期
    current_start = start_date

    while current_start < end_date:
        # 计算当前结束日期
        current_end = current_start + relativedelta(months=1)
        # 确保不超过最终结束日期
        if current_end > end_date:
            current_end = end_date
        # 添加到结果列表
        date_ranges.append((current_start, current_end))
        # 更新当前开始日期
        current_start = current_end

    return date_ranges


def split_into_daily_ranges(start_date, end_date):
    # 确保输入日期为 datetime 对象
    if isinstance(start_date, str):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    if isinstance(end_date, str):
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    # 初始化结果列表
    date_ranges = []

    # 当前开始日期
    current_start = start_date

    while current_start < end_date:
        # 计算当前结束日期
        current_end = current_start + timedelta(days=1)
        # 确保不超过最终结束日期
        if current_end > end_date:
            current_end = end_date
        # 添加到结果列表
        date_ranges.append((current_start, current_end))
        # 更新当前开始日期
        current_start = current_end

    return date_ranges
if __name__ == '__main__':
    # 示例使用
    start = "2020-08-20"
    end = "2024-11-01"
    ranges = split_into_daily_ranges(start, end)
    for r in ranges:
        print(r[0].strftime('%Y-%m-%d'), r[1].strftime('%Y-%m-%d'))
    print(len(ranges))
