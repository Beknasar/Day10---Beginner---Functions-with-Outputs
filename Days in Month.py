def is_leap(year):
  """Check an year for leap"""
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(year, month):
  """Return a days in month. Usage example days_in_month(year=2022, month=2)""" #docstring - пишем документацию к своей функции
  if month > 12 or month < 1:
    return "Invalid month"
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  if is_leap(year) and month == 2:
    return 29
  else:
    return month_days[month - 1]
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)











