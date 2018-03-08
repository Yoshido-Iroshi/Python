import os
import time
import calendar
os.system('cls')
os.system('color b')
cal = calendar.month(2017, 10, 3)
print('\n''\n'"============================")
print("==ANONYMOUS LOCAL CALENDAR=="'\n'"============================")
print('\n' ,cal)
localtime = time.asctime( time.localtime(time.time()) )
print('\n''\n'"    >> CURRENT TIME <<"'\n', localtime, '\n')