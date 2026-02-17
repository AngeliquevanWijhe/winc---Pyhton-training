import datetime as dt

with open('time.txt', 'r') as f:
    current_date = f.readline()

def advance_time(days: int):
    to_datetime = dt.datetime.strptime(current_date, "%Y-%m-%d")
    timedelta = dt.timedelta(days=days)
    new_date = to_datetime + timedelta

    with open('time.txt', "w") as f:
        f.write(new_date.strftime("%Y-%m-%d"))

advance_time(5)