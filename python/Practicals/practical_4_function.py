#######################################################
##
##  Question 1
##
#######################################################

def sumList(nums):
    total = 0
    
    for number in nums:
        total += number


    return total

    

#######################################################
##
##  Question 2
##
#######################################################

def squareEach(nums):
    result = []
    
    for number in nums:
        result += [number * number]
        

    return result



#######################################################
##
##  Question 3
##
#######################################################

def toNumbers(str_list):
    
    list_num = []
    index = 0
    str_num = '' # store substring in between space
    
    while index < len(str_list):
        if(str_list[index] == ' '): # Finished reading a number
            if(len(str_num) > 0):   # Not empty so convert to number
                list_num.append(eval(str_num)) # Add number to list

            str_num = '' # Re-initialise the accumulator

        else:
            str_num += str_list[index] # Keep building a number
            

        index += 1
        
        
    ## Must NOT forget the last number in the list
    if(len(str_num) > 0):   # last number not empty so convert it
        list_num.append(eval(str_num)) # Add number to list
    

    return list_num


#######################################################
##
##  Question 4
##
#######################################################

##file_name = raw_input("Enter the file name: ")
##
##num_file = open(file_name, 'r')
##line = num_file.readline()
##total_sum_square = 0
##
##while len(line) > 0:
##    list_num = toNumbers(line)
##    squares = squareEach(list_num)
##    total_sum_square += sumList(squares)
##
##    # Remember to iterate by reading the next line.
##    # Same idea as doing index += 1
##    line = num_file.readline()
##
##    
##num_file.close() # Good practice to close the file where you opened it.
##
##print "the total is:", total_sum_square
    


#######################################################
##
##  Question 5
##
#######################################################

## Part 1

def feet_to_metric(feet, inches = 0):
    """

    feet_to_metric(feet, inches) --> float

    return the measurement in meter when given the measurement in feet and inches.
    Inches is set by default to 0.

    """
    meter = (feet * 12 + inches) * 0.0254
    return meter

def metric_to_feet(meters):
    """

     metric_to_feet(meter) --> int, int

    return the closet measurement in feet and inches when given the measurement in meters.
    the first value is the number of feet, the second the number of inches.
    
    """
    ## integer division used, as conversion meter to feet not given must use the conversion inch
    ## to meter
    feet = int(meters // (12 * 0.254))
    inches = int(meters % feet)
    return feet, inches


#######################################################
##
##  Problem I
##
#######################################################

## HINTS

## I would use a dictionary to store the data, using a word as a key, and its current number
## of occurences as a value.
##
## You should read one line at a time, transform it into lower case, then split it into a list
## of words (using the split(...) function from a string). For each word in the least, I would
## remove all non alpha-numeric values (you may have to write a function for that).
##
## Then for each word in the list, I would update its current entry in the dictionary if it
## already exist, or add it to the dictionary.
##
## Do that for all line in the file.
##
## For the statistics, I would write one function for each, taking the dictionary as parameter
## and returning the corresponding statistic.


    
#######################################################
##
##  Problem II
##
#######################################################

## HINTS

## Once again I would use a dictionary. I'll add a keyword 'dimension' with a tuple containing its
## dimension as a value (in our case (6,6)).
## example:
##   s = {}
##   s['dimension'] = (6,6)
##
## For each non-zero entries, I would use a tuple(not a list) (row, col) as a key and the entry value
## as value.
## example:
##   s[(1,3)] = 2.0
##   s[(2,2)] = 1.0
##   s[(2,4)] = 1.0
##   ...

## Addition A = M + S: if a key is in matrices S and M, add the two values for that key and store
## the new value into A. For all other keys, add them directly into A with their current value

## Transpose T = transpose(S): for all keys (r,c) with value v in S, add key (c,r) with value v in T
