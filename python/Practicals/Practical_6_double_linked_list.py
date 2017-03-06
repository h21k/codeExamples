

class Node:

    def __init__(self, element):
        self.element = element
        self.previous = None
        self.next = None

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


class DoubleLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        rep = '<DoubleLinkedList: size = ' + str(self.size) + ', '
        if self.head != None:
            rep += ', ' + str(self.head)

        rep += '>'
        return rep

    
    
        
def isempty(linkedList):
    return linkedList.head == None

def size(linkedList):
    return linkedList.size


def printList(linkedList):
    print '<',
    if not isempty(linkedList):
        currentNode = linkedList.head 
        while currentNode != None:
            print currentNode.element, ',',
            currentNode = currentNode .next
    print '>'

            


def add_first(linkedList, element):
    if isempty(linkedList):
        node = Node(element)
        linkedList.head = node
        linkedList.size += 1
    else:
        node = Node(element)
        node.next = linkedList.head
        linkedList.head.previous = node
        linkedList.head = node
        linkedList.size += 1
    

def add_last(linkedList, element):
    if isempty(linkedList):
        node = Node(element)
        node.next = None
        linkedList.head = node
        linkedList.size += 1
    else:
        currentNode = linkedList.head 
        while currentNode.next != None: ## e.g. not the last element in the list
            currentNode = currentNode .next
            
        node = Node(element)
        node.previous = currentNode
        currentNode.next = node
        linkedList.size += 1



def insert_at(linkedList, element, pos):

    if (pos > linkedList.size):
        raise IndexError('list index out of range')
    
    elif pos == 0:
        add_first(linkedList,element)
        
    elif pos == linkedList.size:
        return add_last(linkedList, element)
    
    else:
        currentNode = linkedList.head
        currentIndex = 1
        while currentIndex < pos :
            currentNode = currentNode.next
            currentIndex += 1

        tempPointer = currentNode.next
        newNode = Node(element)
        currentNode.next = newNode
        newNode.previous = currentNode
        newNode.next = tempPointer
        tempPointer.previous = newNode
        linkedList.size += 1
         

def remove_first(linkedList):
    if isempty(linkedList):
        raise IndexError('remove from empty list')
    elif linkedList.size ==1:
        first_element = linkedList.head.element
        linkedList.head = None
        linkedList.size = 0
        return first_element
    else:
        first_element = linkedList.head.element
        linkedList.head = linkedList.head.next
        linkedList.head.previous = None ## Must remember to remove both links
        linkedList.size -= 1
        return first_element

def remove_last(linkedList):
    if isempty(linkedList):
        raise IndexError('remove from empty list')
    elif linkedList.size == 1:
        element = linkedList.head.element
        linkedList.size = 0
        linkedList.head = None
        return element
    else:
        currentNode = linkedList.head
        ## As we have the attribute size, I can use a for loop for a change.
        ## without size I must use a while loop.

        for index in xrange(linkedList.size -2): ## stopping just before the last element
            currentNode = currentNode.next

        tempPointer = currentNode.next ## pointing to the last element
        currentNode.next = None  ## removing first link
        tempPointer.previous = None ## removing second link
        linkedList.size -= 1
        return tempPointer.element
        

def remove_at(linkedList, pos):
    assert linkedList != None, 'Illegal argument None'
    assert pos <= linkedList.size, 'Out-of-bound error'

    if (pos >= linkedList.size):
        raise IndexError('list index out of range')
    
    elif pos == 0:
        return remove_first(linkedList)

    elif pos == linkedList.size - 1:
        return remove_last(linkedList)
        
    else:
        currentNode = linkedList.head
        currentIndex = 1
        while currentIndex < pos :
            currentNode = currentNode.next
            currentIndex += 1

        tempPointer = currentNode.next ## element to remove
        element = tempPointer.element
        tempPointer.next.previous = currentNode
        currentNode.next = tempPointer.next
        tempPointer.next = None
        tempPointer.previous = None
        linkedList.size -= 1
        return element
         

def reverse(linkedList):
    newList = DoubleLinkedList()
    if not isempty(linkedList):
        currentNode = linkedList.head
        while currentNode != None:
            add_first(newList, currentNode.element)
            currentNode = currentNode.next
            
    return newList


#######################################################
##
##                TESTS
##
#######################################################
        
lst = DoubleLinkedList()
print 'is empty:', isempty(lst)

print '\n adding 1 3 4 2',
add_first(lst, 1)
add_first(lst, 3)
add_first(lst, 4)
add_first(lst, 2)

printList(lst)

print '\n insert 10 @ 0, 30 @ 5',

insert_at(lst, 10, 0)
insert_at(lst, 30, 5)

printList(lst)

print '\n add last 40 and 20',

add_last(lst, 40)
add_last(lst, 20)

printList(lst)

print '\n reversed:',
reversed_lst = reverse(lst)

printList(reversed_lst)

print 'remove at 2:', remove_at(reversed_lst,2)
print 'remove last:', remove_last(reversed_lst)
print 'remove first:', remove_first(reversed_lst)

printList(reversed_lst)





























































