'''
Created on Jan 25, 2013
@author: kenobi
v.001
'''
class DVD: #class definition
    identification = 1
    ownedby = "Library"
    def __init__(self, price, title, producer, ISBN): # Constructor
            self.title = title   # attribute
            self.identification = DVD.identification
            DVD.identification += 1    # attribute
            self.price = price # attribute
            self.producer = producer # attribute
            self.price = price # attribute
            self.status = False
            self.ISBN = ISBN # attribute
            self.ownedby = DVD.ownedby 
               
    def __del__(self):
            class_name = self.__class__.__name__
            print (class_name, "destroyed")        
    def __repr__(self):
            print (str(self.title) + " " + str(self.price) + " " + str(self.title) + " " + str(self.identification) + " " + str(self.producer) + " Is the item borrowed:" + str(self.status) + " " + str(self.ISBN) + " The item is curently owned by: " + str(self.ownedby))
    def setPrice(self, new_price): # Method (mutator)
            self.price = new_price
    def setStatus(self, new_status): # Method (mutator)
            self.status = new_status
    def getPrice(self): # Method (accessor)
            return self.price    
    def setIdentificaton(self, new_identification): # Method (accessor)
            self.identification = new_identification
    def getIdentification(self): # Method (accessor)
            return self.identification  
    def getStatus(self): # Method (accessor)
            return self.status  
    def getOwnedby(self): # Method (accessor)
            return self.ownedby 
    def setOwnedby(self, new_ownedby): # Method (accessor)
            self.ownedby = new_ownedby 
    def returned(self): # Method (accessor)
            self.ownedby = "Library" 
# Create a new instance of class Item
first = DVD(10.20, "murata", "JJ Abrams", "0010102028", ) # Constructor Call
second = DVD(9.99, "Susu", "roger", "030020202")
print (first.getPrice()) # method call 
first.setPrice(15.00)  # method call
print (first.getPrice()) 
print (first.getIdentification()) 
print (first.getStatus())
first.setStatus(True) 
print (first.getStatus())
print (second.getIdentification())
print (second.getOwnedby())
first.setOwnedby("Frank") 
second.setOwnedby("Susan") 
print (first.getOwnedby())
print (second.getOwnedby())
first.__repr__()
first.returned()
first.__repr__()
