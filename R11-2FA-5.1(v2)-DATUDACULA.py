import datetime

event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

deadline = datetime.date(year, month, day)
month_name = deadline.strftime("%B")
weekday_name = deadline.strftime("%A")

print("\nFormatted Output:")
print("Event:", event_title.upper())
print("Date:", month_name, str(deadline.day) + ",", deadline.year)
print("Year:", deadline.year)
print("Month:", month_name)
print("Day:", deadline.day)
print("Weekday:", weekday_name)