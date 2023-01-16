'''
File: timeConversion.py
-----
Author: KHALIL HADJI 
'''

import re


def timeConversion(s):
    period_pattern = r"PM|AM"
    time_pattern = r"\d{2}:\d{2}:\d{2}"
    period = re.search(pattern=period_pattern, string=s).group()
    time = re.search(pattern=time_pattern, string=s).group()
    hours = int(time[:2])
    if period == "AM":
        if hours >= 12:
            hours -= 12
    elif period == "PM":
        if hours < 12:
            hours += 12
    if hours < 10:
        hours = f"0{hours}"
    return f"{hours}" + time[2:]
