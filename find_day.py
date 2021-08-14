import calendar
date = input("Enter a date(dd/mm/yyyy):")
year = int(date[6:])
month = int(date[3:5])
day = int(date[:2])
weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
result =(calendar.weekday(year, month, day))
print(weekDays[result])



