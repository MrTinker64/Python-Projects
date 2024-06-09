def add_0(minutes):
    if minutes < 10:
        return "0" + str(minutes)
    else:
        return str(minutes)

hour1, minute1 = input("time1: ").split(":")
time2 = input("time2: ")
try:
    hour2, minute2 = time2.split(":")
except ValueError:
    hour2 = time2
    minute2 = 0
total_minutes = (int(hour1) * 60) + int(minute1) + (int(hour2) * 60) + int(minute2)
remainder_minutes = total_minutes % 60
total_hours = total_minutes // 60 % 12

# print(f"Hour1 = {hour1}, Minute1 = {minute1}\nHour2 = {hour2}, Minute2 = {minute2}")
print(f"New time: {total_hours}:{add_0(remainder_minutes)}")