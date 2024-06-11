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
        time, am_pm = inputTime.split(" ")
        hour, minute = time.split(":")
    except ValueError:
        am_pm = ""
        hour, minute = inputTime.split(":")
    if am_pm == "PM":
        hour = int(hour) + 12
    return int(hour), int(minute)

hour1, minute1 = get_time(1)
hour2, minute2 = get_time(2)
total_minutes = ((hour2 * 60) + minute2) - ((hour1 * 60) + minute1)
remainder_minutes = total_minutes % 60
total_hours = (total_minutes // 60) % 24 or 12

print(f"Time difference: {total_hours}:{add_0(remainder_minutes)}")