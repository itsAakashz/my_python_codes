#Python Program to Display Current time

import calendar
from datetime import datetime

sam = datetime.now()
current_time = sam.strftime("%H:%M:%S")
print(current_time)
