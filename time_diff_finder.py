def add_0(minutes):
    if minutes < 10:
        return "0" + str(minutes)
    else:
        return str(minutes)
    
def get_time(index):
    inputVar = input(f"time{index}: ")
    try:
        time, am_pm = inputVar.split(" ")
        hour, minute = time.split(":")
    except ValueError:
        am_pm = ""
        hour, minute = inputVar.split(":")
    if am_pm == "PM":
        hour = int(hour) + 12
    return hour, minute, am_pm
        

hour1, minute1, am_pm1 = get_time(1)
hour2, minute2, am_pm2 = get_time(1)
total_minutes = ((int(hour2) * 60) + int(minute2)) - ((int(hour1) * 60) + int(minute1))
remainder_minutes = total_minutes % 60
total_hours = (total_minutes // 60) % 12 or 12

# print(f"Hour1 = {hour1}, Minute1 = {minute1}\nHour2 = {hour2}, Minute2 = {minute2}")
print(f"Time difference: {total_hours}:{add_0(remainder_minutes)}")

# TODO need to actually make this work.