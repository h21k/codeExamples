#######################################################
##
##  Question 1
##
#######################################################

## Part 1

##text = raw_input("Enter a string: ")
##
##for letter in text:
##    code = ord(letter)
##    print letter + "--> ", str(code)

#######################################################
## Part 2

##text = raw_input("Enter a string: ")
##
##total = 0
##
##for letter in text:
##    total += ord(letter)
##
##print text + "--> ", str(total)



    

#######################################################
##
##  Question 2
##
#######################################################

##text = raw_input("Enter a sentence of a word: ")
##
#### transform to lower case in case there is upper and lower case in the sentence
##text = text.lower()
##
##palindrome = True ## We will try to proove it wrong
##reverse_index = 0
##
##for letter in text:
##    if(letter != text[-1 - reverse_index]):
##        palindrome = False
##        break;
##    else:
##        reverse_index += 1
##        
##
##if(palindrome):
##    print text + " is a palindrome."
##else:
##    print text + " is not a palindrome."
##
#### NOTE: THIS CODE IS NOT OPTIMAL. WHY?
#### CAN YOU CHANGE IT TO MAKE IT OPTIMAL?



#######################################################
##
##  Question 3
##
#######################################################

## Part 1

##vector = eval(raw_input("Enter a vector [x, y, ..]: "))
##scalar = float(raw_input("Enter a scalar: "))
##
##prod = []
##
##for number in vector:
##    prod = prod + [number * scalar]
##
##print prod
    
## DON'T FORGET TO TEST WITH THE EMPTY VECTOR []


#######################################################
## Part 2

##vector1 = eval(raw_input("Enter a vector [x, y, ..]: "))
##vector2 = eval(raw_input("Enter a vector [x, y, ..]: "))
##
##if(len(vector1) == len(vector2)):
##    sum_vector = []
##    index = 0
##    while index < len(vector1):
##        sum_vector = sum_vector + [vector1[index] + vector2[index]]
##        index +=1
##
##    print vector1, "+", vector2, '=', sum_vector
##else:
##    print "cannot add vectors with different dimensions."
    


#######################################################
##
##  Question 4
##
#######################################################

#### printing the header of table
##print '| st\\lb',
##for lb in range(0, 14):
##    print '| %4.0f'%lb,
##
##print '|' # no comma here to return to the line, end of row
##    
##print '|------',
##for i in range(0, 14):
##    print '|-----',
##
##print '|' # no comma here to return to the line, end of row
##
#### end of printing header
##    
##for st in range(0, 15):
##    print '|  %4.0f'%st, # printing the first column
##    
##    for lb in range(0, 14):
##        kg = st * 6.35 + lb * 0.45
##        print '| %4.1f'%kg,
##
##    print '|' # no comma here to return to the line, end of row
##
##



#######################################################
##
##  Question 5
##
#######################################################

## we represent a matrice using a list of lists
## e.g. a row is represented by a list
## a matrice is represented by a list of rows
##
## A = [[a11, a12], [a21, a22], [a31, a32]]
##
## To get a21, second row, first column we use A[1][0],
## remember the first row is at index 0 not 1.
##
## WE ASSUME ALL ENTERED MATRICES ARE WELL FORMED,
## E.G. ALL ROWS HAVE THE SAME NUMBER OF COLUMNS


## SCALAR PRODUCT ##############################

##matrix = eval(raw_input("Enter a matrix [[a11, a12], [a21, a22],..]: "))
##scalar = float(raw_input("Enter a scalar: "))
##
##prod = []
##
##for row in matrix:
##    new_row = []
##    for number in row:
##        new_row = new_row + [number * scalar]
##        
##    prod = prod + [new_row] # must encapsulate the row into the matrix hence []
##
##print prod


#### ADDITION  ######################################
##
##matrix1 = eval(raw_input("Enter a matrix [[a11, a12], [a21, a22],..]: "))
##matrix2 = eval(raw_input("Enter a matrix [[a11, a12], [a21, a22],..]: "))
##
#### Must check matrices are compatible for addition
##compatible = True
##
##if(len(matrix1) != len(matrix2)): # Not having same number of rows
##    compatible = False
##else:
##    row = 0;
##    while row < len(matrix1):
##        if(len(matrix1[row]) != len(matrix2[row])):
##            # not having the same number of columns
##            compatible = False
##            break
##
##        row += 1
##    
#### perform addition if compatible matrices
##if(compatible):
##    sum_mat = []
##
##    row = 0;
##    while row < len(matrix1):
##        col = 0
##        sum_row = []
##        while col < len(matrix1[row]):
##            sum_row = sum_row + [matrix1[row][col] + matrix2[row][col]]
##            col += 1
##
##        sum_mat += [sum_row] # must encapsulate the row into the matrix hence []
##        row += 1
##            
##    print sum_mat
##else:
##    print "cannot perform addition on matrices with different dimensions."


## TRANSPOSE  ###########################################
## WE ASSUME THAT THE MATRIX HAS AT LEAST ONE ROW & IS WELL FORMED

##matrix = eval(raw_input("Enter a matrix [[a11, a12], [a21, a22],..]: "))
##
##transpose = []
##
##row_dim = len(matrix)
##col_dim = len(matrix[0])
##
##col = 0
##while col < col_dim:
##    trans_row = []
##    row = 0
##    while row <row_dim:
##        trans_row = trans_row + [matrix[row][col]]
##        row += 1
##
##    transpose = transpose + [trans_row]
##    col += 1
##
##print transpose



#######################################################
##
##  Question 6
##
#######################################################

##
##grain_weight = 30 #in mg
##current_square = 1 #first square initialised
##total_grain = 1
##for index in range(2,65) : #counting from second square and 65 not included
##    current_square *= 2
##    total_grain += current_square
##
##    # a nice presentation
##    if(current_square * 30 < 1e3):
##        print 'the weight on square', index, 'is', str(current_square * 30),'mg.'
##    elif(current_square * 30 < 1e6):
##        print 'the weight on square', index, 'is', str(current_square * 30 / 1e3),'g.'
##    elif(current_square * 30 < 1e9):
##        print 'the weight on square', index, 'is', str(current_square * 30 / 1e6),'kg.'
##    elif(current_square * 30 < 1e15):
##        print 'the weight on square', index, 'is', str(current_square * 30 / 1e9),'tons.'
##    elif(current_square * 30 < 1e18):
##        print 'the weight on square', index, 'is', str(current_square * 30 / 1e15),'million tons.'
##    elif(current_square * 30 < 1e21):
##        print 'the weight on square', index, 'is', str(current_square * 30 / 1e18),'billion tons.'
##    else:
##        print 'the weight on square', index, 'is', str(current_square * 30 / 1e21),'trillion tons.'
##        
##
##total_weight = total_grain *30 #in mg
##
##if(total_weight < 1e3):
##    print 'the total weight is:', str(total_weight),'mg.'
##elif(total_weight < 1e6):
##    print 'the total weight is:', str(total_weight/1e3),'g.'
##elif(total_weight < 1e9):
##    print 'the total weight is:', str(total_weight/1e6),'kg.'
##elif(total_weight < 1e15):
##    print 'the total weight is:', str(total_weight/1e9),'tons.'
##elif(total_weight < 1e18):
##    print 'the total weight is:', str(total_weight/1e15),'million tons.'
##elif(total_weight < 1e21):
##    print 'the total weight is:', str(total_weight/1e18),'billion tons.'
##else:
##    print 'the total weight is:', str(total_weight/1e21),'trillion tons.'
##
##print 'Which is equivalent to', (total_weight / 678e15),'years of the world wide production.'




    
#######################################################
##
##  Problem I
##
#######################################################

##I deliberately chose to check the input from user in the first menu
##and to break the program in the sub-menus if the input was incorrect.
##It is a way to show you how you can flag errors and control some type
##of errors. We will learn more about error control later this term.
##
##Another possibility is to use another loop inside the if-else statements to control the
##user inputs in the sub-menus.



price = 0

while True:
    print "Select the type of item to rent:"
    print "\t 1 - Movie"
    print "\t 2 - Game"
    print "\t 3 - Exit"

    type_item = raw_input("Enter your choice: ")

    if (type_item == '1'):
        # We are in the movie selection
        # Create menu for movie
        print "Select the media:"
        print "\t 1 - DVD"
        print "\t 2 - Blue-Ray"

        media = raw_input("Enter your choice: ")

        if (media == '1'):
            price += 2.5
        elif (media == '2'):
            price += 3.5
        else:
            price = -1 # I use -1 as a flag for a incorrect input
            break

    elif  (type_item == '2'):
        # We are in the game selection
        # Create menu for game
        print "Select the tariff:"
        print "\t 1 - New Release"
        print "\t 2 - Standard"

        media = raw_input("Enter your choice: ")

        if (media == '1'):
            price += 4.0
        elif (media == '2'):
            price += 2.5
        else:
            price = -1 # I use -1 as a flag for a incorrect input
            break

    elif (type_item == '3'): #exit the menu
        break
    
    else:
        print "The choice you made was not recognised"
        continue # restart at the begining of the iteration for another input



if (price == -1):
    # Flag for "An input error has occurred"
    print 'An Error has occurred'
elif (price == 0):
    print 'You have not purchased any item.'    
else:
    print 'The final bill is \xa3'+str(price)


