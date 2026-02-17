import datetime
import pytz

today_datetime=datetime.datetime.today()
today_string="2025-02-17"

datetime_to_string = today_datetime.strftime("%Y-%m-%d")
print(datetime_to_string)

string_to_datetime = datetime.datetime.strptime(today_string, "%Y-%m-%d")
print(string_to_datetime)

today_date = datetime.date.today()
timedelta = datetime.timedelta(days=20)
print(today_date)
date_after_20_days = today_date + timedelta
print(date_after_20_days)

new_years = datetime.date(2026,12,31)
till_new_years = new_years - today_date
print(till_new_years)

dt = datetime.datetime(2026, 2, 23, 18, 15, 23, tzinfo=pytz.timezone("Europe/Amsterdam"))
print(dt)

# for tz in pytz.all_timezones:
#     print(tz)