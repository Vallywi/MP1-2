# Exercise 26 - Current Time

import time

def show_current_time():
    current_time = time.localtime()
    readable_time = time.asctime(current_time)
    print("Current date and time:")
    print(readable_time)

show_current_time()