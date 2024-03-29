#!/bin/bash/env python3

import datetime

str_date_list = [
    "2018/01/01",
    "2018/01/02",
    "2018/01/03",
    "2018/01/04",
    "2018/01/05",
    "2018/01/06",
    "2018/01/07",
    "2018/01/08",
    "2018/01/09",
    "2018/01/10",
    "2018/01/11",
    "2018/01/12",
    "2018/01/13",
    "2018/01/14",
    "2018/01/15",
    "2018/01/16",
    "2018/01/17",
    "2018/01/18",
    "2018/01/19",
    "2018/01/20",
    "2018/01/21",
    "2018/01/22",
    "2018/01/23",
    "2018/01/24",
    "2018/01/25",
    "2018/01/26",
    "2018/01/27",
    "2018/01/28",
    "2018/01/29",
    "2018/01/30",
    "2018/01/31",
    "2018/02/01",
    "2018/02/02",
    "2018/02/03",
    "2018/02/04",
    "2018/02/05",
    "2018/02/06",
    "2018/02/07",
    "2018/02/08",
    "2018/02/09",
    "2018/02/10",
    "2018/02/11",
    "2018/02/12",
    "2018/02/13",
    "2018/02/14",
    "2018/02/15",
    "2018/02/16",
    "2018/02/17",
    "2018/02/18",
    "2018/02/19",
    "2018/02/20",
    "2018/02/21",
    "2018/02/22",
    "2018/02/23",
    "2018/02/24",
    "2018/02/25",
    "2018/02/26",
    "2018/02/27",
    "2018/02/28",
    "2018/03/01",
    "2018/03/02",
    "2018/03/03",
    "2018/03/31",
    "2018/04/01",
    "2018/04/02",
    "2018/04/03",
    "2018/04/04",
    "2018/04/05",
    "2018/04/06",
    "2018/04/07",
    "2018/04/08",
    "2018/04/09",
    "2018/04/10",
    "2018/04/23",
    "2018/04/24",
    "2018/04/25",
    "2018/04/26",
    "2018/04/27",
    "2018/04/28",
    "2018/04/29",
    "2018/04/30",
    "2018/05/01",
    "2018/05/02",
    "2018/05/03",
    "2018/05/04",
    "2018/05/05",
    "2018/05/06",
    "2018/05/07",
    "2018/05/08",
    "2018/05/09",
    "2018/05/10",
    "2018/05/28",
    "2018/06/03",
    "2018/06/04",
    "2018/06/05",
    "2018/06/06",
    "2018/06/29",
    "2018/07/01",
    "2018/07/24",
    "2019/07/25",
    "2019/07/26",
    "2019/07/27",
    "2019/09/22",
    "2019/09/23",
    "2019/09/24",
    "2019/09/25",
    "2019/09/26",
    "2019/12/27",
    "2019/12/28",
    "2019/12/29",
    "2020/03/01",
    "2020/03/02",
    "2020/03/03",
    "2020/03/31",
    "2022/10/01",
    "2022/10/02",
    "2022/10/31",
    "2022/11/01",
]

date_list = []
for d in str_date_list:
    date = datetime.datetime.strptime(d, "%Y/%m/%d")
    date_list.append(date)

print(f"date_list:\n{date_list}")

last_month_dates = []
for _ in range(len(date_list)):
    first_date = date_list[0]
    if len(date_list) == 1:
        last_month_dates.append(first_date)
        break
    second_date = date_list[1]
    if (first_date.year == second_date.year and first_date.month != second_date.month) or (
        first_date.year != second_date.year and first_date.month != second_date.month):
        last_month_dates.append(first_date)
        date_list.pop(0)
    else:
        date_list.pop(0)

print(f"last_month_dates:\n{last_month_dates}")
str_last_month_dates = [datetime.datetime.strftime(d, "%Y/%m/%d") for d in last_month_dates]
print(f"str_last_month_dates:\n{str_last_month_dates}")
