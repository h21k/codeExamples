####Q1
##def print_pattern(n):
##    string=""
##    for row in range(1,n+1):
##        for column in range(row):
##            string = ("o")*column + "x" *(n-column)
##        print string
##
##print_pattern(5)
##print "..........................."
##print_pattern(4)

#Q2

class Item:
    def __init__(self, barcode, price_per_unit, number_of_units, VAT_rate):
        self.__barcode= barcode
        self.__price_per_unit = price_per_unit
        self.__number_of_units= number_of_units
        self.__VAT_rate = VAT_rate

    def get_barcode(self):
        return self.__barcode
    def get_price_per_unit(self):
        return self.__price_per_unit
    def get_number_of_units(self):
        return self.__number_of_units
    def get_VAT_rate(self):
        return self.__VAT_rate
    def change_price_per_unit(self, new_price):
        self.__price_per_unit = new_price
    def decrease_number_of_units(self, decrease_by): # when item is sold, this can decrease
        self.__number_of_units-= decrease_by        #number of its units
    def change_VAT_rate(self,VAT_rate):
        self.__VAT_rate = VAT_rate
        

    def __repr__(self):
        return ("<Item, barcode: "+ str(self.__barcode) + ", price per unit: " +str(self.__price_per_unit)
                + ", number of units: " +str(self.__number_of_units) + ", VAT rate: "
                + str(self.__VAT_rate) + " >")

class Grocery(Item):

    def __init__(self, barcode,price_per_unit,number_of_units, VAT_rate, sell_by, best_before):
        Item.__init__(self, barcode,price_per_unit, number_of_units, VAT_rate)
        self.__sell_by=sell_by
        self.__best_before= best_before
        self.__barcode= barcode
        self.__price_per_unit = price_per_unit
        self.__number_of_units= number_of_units
        self.__VAT_rate = VAT_rate

        def get_best_before(self):
            return self.__best_before
        def get_sell_by(self):
            return self.__sell_by
        
    def __repr__(self):
        return ("<Grocery,barcode: "+ str(self.__barcode) + ", price per unit: " +str(self.__price_per_unit)
                + ", number of units: " +str(self.__number_of_units) + ", VAT rate: "
                + str(self.__VAT_rate) + ", sell by: " + str(self.__sell_by) + ", best_before: "
                + str(self.__best_before) + ">")

class Electronic(Item):
    def init__(self, barcode, price_per_unit, number_of_units, VAT_rate, brand, warranty):
        self.__barcode= barcode
        self.__price_per_unit = price_per_unit
        self.__number_of_units= number_of_units
        self.__VAT_rate = VAT_rate
        self.__brand=brand
        self.__warranty=warranty

        def get_brand(self):
            return self.__brand
        def get_warranty(self):
            return self.__warranty
        
    def __repr__(self):
        return ("<Item, barcode: "+ str(self.__barcode) + ", price per unit: " +str(self.__price_per_unit)
                + ", number of units: " +str(self.__number_of_units) + ", VAT rate: "
                + str(self.__VAT_rate)+ ", brand: " +str(self.__brand) +
                ", warranty: " +str(self.__warranty)+ " >")
                
                


class Basket:
    def __init__(self):
        self.__items ={}
        self.__price =0
    
    def __repr__(self):
        return "<Basket, items: " +str(self.__items) + ", price: " + str(self.__price + " >")
    
    def add_item(barcode, price_per_unit, number_of_units, VAT_rate):
##        if contains_item(barcode, basket):
##            return "Item already exists"
##        else:
            new_item = Item(barcode, price_per_unit, number_of_units, VAT_rate)
            basket.__items[barcode] = new_item
            return new_item

    def get_items(self):
        return self.__items
    def contains_item(barcode, basket):
        return (barcode in self.get_items.keys())
    
    def remove_item(barcode, basket):
        if (not contains_item(barcode,basket)):
            return "no such item"
        else:
            del (basket.get_items(self))[barcode]
        
        
        
        
    
my_grocery = Grocery("barcode","price_per_unit","number_of_units", "VAT_rate", "sell_by", "best_before")
print my_grocery

