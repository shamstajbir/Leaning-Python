import calendar
year, month = int(input("Year: ")), int(input("Month: "))
print(calendar.TextCalendar().formatmonth(year, month))
