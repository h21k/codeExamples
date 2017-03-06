'''
Created on Oct 22, 2012

@author: kenobi
'''
#######################################################
##
##  Problem I
##
#######################################################

print ("Select the type of item to rent:")
print ("\t 1 - Movie")
print ("\t 2 - Game")

type_item = input("Enter your choice: ")

if (type_item == '1'):
    # We are in the movie selection
    # Create menu for movie
    print ("Select the media:")
    print ("\t 1 - DVD")
    print ("\t 2 - Blue-Ray")

    media = input("Enter your choice: ")

    if (media == '1'):
        price = 2.5
    elif (media == '2'):
        price = 3.5
    else:
        price = -1 # I use -1 as a flag for a incorrect input

elif  (type_item == '2'):
    # We are in the game selection
    # Create menu for game
    print ("Select the tariff:")
    print ("\t 1 - New Release")
    print ("\t 2 - Standard")

    media = input("Enter your choice: ")

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
    print ('An Error has occurred')
else:
    print ('The final bill is \xa3'+str(price))