#!/usr/bin/python

import argparse
import sys
import os, time

def main(argv):
    
    #####This block parses the command line arguments#########
    
    parser = argparse.ArgumentParser()
    #Add the two arguments.
    parser.add_argument("inputfile",
                        help="The file from which the timestamps will be copied.")
    parser.add_argument("target",
                        help="The target file or directory.")
    args = parser.parse_args() #do the parsing.

    inputfile = args.inputfile #Dump the command line arguments into variables.
    target = args.target

    ##############End of parsing block########################
    
    #The real functionality starts here.

    def visit(arg, dirname, names):#This function is executed if the target is a dir.
        #arg is an arbitrary parameter.
        #dirname is a path to a directory
        #names is a list with the filenames for the directory 'dirname'
        
        for file_name in names: #For each file in the directory...
            path = dirname + "/" + file_name
            os.utime(path ,(atime,mtime)) #...update the timestamps. os.utime() is the function that does the trick. 
        return #End of the visit function

    
    #Initialize variable. The important ones: atime, mtime. 
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=(0,0,0,0,0,0,0,0,0,0)

    if os.path.exists(inputfile): #Check if the inputfile exists
        #Ok, the input file exists. Now lets read the attributes for that file with os.stat.
          (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(inputfile)
    else:
        #Error. The inputfile doesn't exist. Print a message and terminate.
        print "{} does not exist.".format(inputfile)
        return


    #Now check if the target exists.
    if os.path.exists(target):
        #Ok, target exists. Now check if it is a directory or a file.

        if os.path.isdir(target): #isdir checks if the path is a directory or not.
            #It must be a directory. 
            #os.path.walk explores recursively the directory 'target'
            #and calls the function 'visit' in each subdirectory 
            os.path.walk(target, visit, target)
        else:  
            #It must be a file then.
            os.utime(target,(atime,mtime)) #The access and modif. timestamps of the target file are updated with os.utime.
                
    else:
        #Error: The target file doesn't exist. Terminate.
        print "{} does not exist.".format(target)
        return
    
    

if __name__ == "__main__":
    main(sys.argv[1:]) #Call the main function.
