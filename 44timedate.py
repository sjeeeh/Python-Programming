import time
import datetime
now=datetime.datetime.now()
print("Current date and time:",now)
print("Current year:",now.year)
print("Month of year:",now.month)
print("Week no of the year:",now.strftime("%U"))
print("Weekday of the week",now.strftime("%A"))
print("Day of the year:",now.strftime("%j"))
print("Day of month:",now.day)
print("Day of week:",now.weekday())
