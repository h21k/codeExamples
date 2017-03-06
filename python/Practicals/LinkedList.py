

class Node:

    def __init__(self, element):
        self.element = element ## should contains an int value
        self.next = None       ## contains a Node object

    def __repr__(self):
        ## This method is recursive, you could use a while loop instead
        rep = '<Node: '
        rep += str(self.element)
        if self.next != None:
            ## the following statement is the recursive call. <str(self.next)> calls
            ## the __repr__ of the next node, hence the recursive nature of this method.
            rep += ', ' + str(self.next)

        rep += '>'
        return rep


class LinkedList:

    def __init__(self):
        self.head = None    ## contains a Node object
        self.size = 0

    def __repr__(self):
        rep = '<LinkedList: (size = ' + str(self.size) + '), elements: '
        if self.head != None:
            currentNode = self.head 
            while currentNode != None:
                rep +=  str(currentNode.element) + ', '
                currentNode = currentNode .next

        rep += '>'
        return rep

class SortedLinkedList:
    
    def __init__(self):
        self.head = None    ## contains a Node object
        self.size = 0

    def __repr__(self):
        rep = '<SortedLinkedList: (size = ' + str(self.size) + '), elements: '
        if self.head != None:
            currentNode = self.head 
            while currentNode != None:
                rep +=  str(currentNode.element) + ', '
                currentNode = currentNode .next

        rep += '>'
        return rep
    
        
def isempty(linkedList):
    return linkedList.head == None

def size(linkedList):
    return linkedList.size


def add_first(linkedList, element):
    node = Node(element)
    node.next = linkedList.head
    linkedList.head = node
    linkedList.size += 1
    
##############################################
##
##                 QUESTION 4
##
##############################################

## WRITE CODE HERE









##############################################
##
##                 QUESTION 5
##
##############################################

## WRITE CODE HERE






#######################################################
##
##                TESTS
##
#######################################################
        
lst = LinkedList()
add_first(lst, 1)
add_first(lst, 3)
add_first(lst, 4)
add_first(lst, 2)





























































