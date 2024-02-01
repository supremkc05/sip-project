import time
time = time.striftime('%H:%M:%S')
print("current time in HH:MM:SS format:",time)
hour=int(time.striftime('%H'))
print(hour)
if (hour>=0 and hour<12):
    print("Good morning!")
elif( hour >=12 and hour<17):
    print("Good afternoon.")
else:
    print("Good night.")
