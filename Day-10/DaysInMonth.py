
def is_leap(year):

    if year%4==0:
     if year % 100 == 0:
      if year%400==0:
        return True
      else:
         return  False

     else:
      return True
    else:
     return False
def months_in_year(year, month):

    months_days=[31,28,31,30,31,30,31,31,30,31,30,31]
    if is_leap(year) and month==2:
        return 29
    else:
       return  months_days[month-1]

year=int(input("Which year do you want to test?"))
month=int(input("Enter the month you would like to test?"))
output=months_in_year(year,month)
print(output)
