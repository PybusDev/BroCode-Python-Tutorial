import datetime

date = datetime.date(2025, 1, 2)
today = datetime.date.today()

time = datetime.time(12, 30, 0)
now = datetime.datetime.now()

now = now.strftime("%Y-%m-%d %H:%M:%S")

target_datetime = datetime.datetime(2030, 1, 2, 12, 30, 1)
current_datetime = datetime.datetime.now()

print(now)

print(target_datetime)

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")