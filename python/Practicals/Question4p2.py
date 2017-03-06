'''
Created on Oct 18, 2012

@author: kenobi
'''
year = int(input("Enter the year: "))

leap_year = True # We assume it is a leap year and try to prove it wrong

if(year % 4 != 0):
    leap_year = False

elif(year % 100 == 0 and not(year % 400 == 0)):
        leap_year = False


if(leap_year):
    print(str(year), "is a leap year.")

else:
    print(str(year), "is not a leap year.")

## Tests:
## year = 1, 1800, 4, and 2000




##date = raw_input("Enter a date (DD/MM/YYYY): ")
##
##[dd, mm, yyyy] = date.split('/')
##day = int(dd)
##month = int(mm)
##year = int(yyyy)
##
##month31 = [1, 3, 5, 7, 8, 10, 12]   # List of months with 31 days.
##month30 = [2, 4, 6, 9, 11]          # List of months with 30 days
##
##valid_date = True # We assume it is a valid date and try to prove it wrong
##
##if (day < 1 or month < 1 or month > 12 or year < 0):
##    valid_date = False
##    
##else:
##    if (month in month31 and day > 31):
##        valid_date = False
##    elif (month in month30 and day > 30):
##        valid_date = False
##    elif (month == 2): #february
##        leap_year = True # We assume it is a leap year and try to prove it wrong
##
##        ## Must check if it is a leap year
##        if(year % 4 != 0):
##            leap_year = False
##
##        elif(year % 100 == 0 and not(year % 400 == 0)):
##            leap_year = False
##
##        if (leap_year and day > 29):
##            valid_date = False
##
##        elif (not leap_year and day >28):
##            valid_date = False
##
##if(valid_date):
##    print date, "is a valid date."
##else:
##    print date, "is not a valid date."

##    print date, "is not a valid date."