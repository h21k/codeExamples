'''
Created on Jan 25, 2013
@author: kenobi
v.001
'''
class DVD: #class definition
    status = False
    unique = 0
    def __init__(self, identification, price, title, producer, status, ISBN): # Constructor
            self.name = title   # attribute
            self.identification = identification    # attribute
            self.price = price # attribute
            self.price = producer # attribute
            self.price = price # attribute
            self.status = status
            self.price = ISBN # attribute
               
    def __del__(self):
            class_name = self.__class__.__name__
            print (class_name, "destroyed")        
#    def __repr__(self):

    def setPrice(self, new_price): # Method (mutator)
            self.price = new_price
    def getPrice(self): # Method (accessor)
            return self.price    
    def setIdentificaton(self, new_identification): # Method (accessor)
            self.identification = new_identification
    def getIdentification(self): # Method (accessor)
            return self.identification  
    def getStatus(self): # Method (accessor)
            return self.status  
# Create a new instance of class Item
first = DVD("001", 10.20, "murata", "JJ Abrams", "True" , "0010102020") # Constructor Call
print (first.getPrice()) # method call 
first.setPrice(15.00)  # method call
print (first.getPrice()) 
print (first.getIdentification()) 
first.setIdentificaton("002")
print (first.getIdentification()) 
print (first.getStatus()) 
del first
