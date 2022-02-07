from datetime import datetime

currtime = datetime.now()

for i in range(10000):
    a = 1

deltime = datetime.now() - currtime

print(str(deltime) + \
    ' the end.')