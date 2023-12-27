###########################
Time
By: Sai Mahesh
21 DEC 2023
'''

from datetime import datetime as dt
# Get the current time, returns a value like 2021-06-21 14:32:21.13125555
today = dt.now()
print(today)
# Get Unix time, returns a value like 13345567.1432785
unix_epoch_time = dt.timestamp(today)
print(unix_epoch_time)
