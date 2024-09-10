from datetime import datetime

def add_0(minutes):
    if minutes < 10:
        return "0" + str(minutes)
    else:
        return str(minutes)

def get_time(index: int):
    inputTime = input(f"time{index}: ")
    if inputTime == "":
        current_time = datetime.now().strftime('%H:%M')
        inputTime = current_time
    
    try:
        time, am_pm = inputTime.split()
    except ValueError:
        am_pm = ""
        time = inputTime
        
    try:
        hour, minute = time.split(":")
    except ValueError:
        hour = time
        minute = 0

    if am_pm.lower() == "pm":
            hour = int(hour) + 12

    try:
        return int(hour), int(minute)
    except ValueError:
        return 0, int(minute)

hour1, minute1 = get_time(1)
hour2, minute2 = get_time(2)
total_minutes = (int(hour1) * 60) + int(minute1) + (int(hour2) * 60) + int(minute2)
remainder_minutes = total_minutes % 60
total_hours = total_minutes // 60 % 12 or 12

print(f"New time: {total_hours}:{add_0(remainder_minutes)}")