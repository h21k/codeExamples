#######################################################
##
##  Question 1
##
#######################################################

##number1 = float(raw_input("Enter your first number: "))
##number2 = float(raw_input("Enter your second number: "))
##number3 = float(raw_input("Enter your third number: "))
##
##max = number1
##
##if(max < number2):
##    max = number2
##
##if(max < number3):
##    max = number3
##
##print "The greatest number is:", str(max)
##
#### To cover all cases I need six tests:
#### number1 < number2 < number3
#### number1 < number3 < number2
#### number2 < number1 < number3
#### number2 < number3 < number1
#### number3 < number2 < number1
#### number3 < number1 < number3
##    



#######################################################
##
##  Question 2
##
#######################################################

##hours = int(raw_input("Enter the number of hours worked: "))
##rate = float(raw_input("Enter the hourly rate \xa3/h: "))
##
##if(hours < 0 or rate < 0):
##    print "Error: incorrect inputs"
##    
##elif (hours > 40):
##    extra = (hours - 40) * 1.5 * rate
##    wages = 40 * rate + extra
##    print "Your wages for this week is \xa3" + str(wages)
##    print "\t including \xa3" + str(extra) + " overtime."
##    
##else:
##    wages = hours * rate
##    print "Your wages for this week is \xa3" + str(wages)





#######################################################
##
##  Question 3
##
#######################################################

##limit = float(raw_input("Enter the speed limit: "))
##speed = float(raw_input("Enter the clocked speed: "))
##
##if(limit < 0 or speed < 0 or limit >= 90):
##    print "Error: incorrect inputs"
##    
##elif (speed > limit):
##    fine = 100 + (speed - limit) * 5
##    if(speed > 90):
##        fine += 200
##
##    print "Your fine is \xa3" + str(fine) +"!"
##
##else:
##    print "Your speed was under the speed limit."
##
##
#### Tests:
#### speed <= 90 and limit < speed
#### speed > 90 and limit < speed
#### speed <= limit




#######################################################
##
##  Question 4
##
#######################################################


##################################################
## Part 1

##year = int(raw_input("Enter the year: "))
##
##leap_year = True # We assume it is a leap year and try to prove it wrong
##
##if(year % 4 != 0):
##    leap_year = False
##
##elif(year % 100 == 0 and not(year % 400 == 0)):
##        leap_year = False
##
##
##if(leap_year):
##    print str(year), "is a leap year."
##
##else:
##    print str(year), "is not a leap year."
##
#### Tests:
#### year = 1, 1800, 4, and 2000



##################################################
## Part 2

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
    


#######################################################
##
##  Problem I
##
#######################################################

print "Select the type of item to rent:"
print "\t 1 - Movie"
print "\t 2 - Game"

type_item = raw_input("Enter your choice: ")

if (type_item == '1'):
    # We are in the movie selection
    # Create menu for movie
    print "Select the media:"
    print "\t 1 - DVD"
    print "\t 2 - Blue-Ray"

    media = raw_input("Enter your choice: ")

    if (media == '1'):
        price = 2.5
    elif (media == '2'):
        price = 3.5
    else:
        price = -1 # I use -1 as a flag for a incorrect input

elif  (type_item == '2'):
    # We are in the game selection
    # Create menu for game
    print "Select the tariff:"
    print "\t 1 - New Release"
    print "\t 2 - Standard"

    media = raw_input("Enter your choice: ")

    if (media == '1'):
        price = 4.0
    elif (media == '2'):
        price = 2.5
    else:
        price = -1 # I use -1 as a flag for a incorrect input

else:
    price = -1 # I use -1 as a flag for a incorrect input


if (price == -1):
    # Flag for "An input error has occurred"
    print 'An Error has occurred'
else:
    print 'The final bill is \xa3'+str(price)
