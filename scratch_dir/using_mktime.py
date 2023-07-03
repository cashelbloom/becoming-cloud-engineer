import datetime
import time
import pandas as pd

match_start_date = '7/2/2023 13:00:00'
timestamp = int(time.mktime(time.strptime(match_start_date, '%m/g%d/%Y %H:%M:%S')))
print(f'this is the timestamp value: {timestamp}')
print(f'This shows the number of seconds in 24 hours: {60 * 60 * 24}')
print(f'After adding one day to 07/02/23, the total seconds for the next day is: {timestamp + 86400}')
print(f'Now using pandas package, the date is: {datetime.datetime.fromtimestamp(timestamp + 86400)}')