

class Node:

    def __init__(self, element):
        self.element = element
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


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def __repr__(self):
        rep = '<LinkedList: size = ' + str(self.size) + ', '
        if self.head != None:
            rep += ', ' + str(self.head)

        rep += '>'
        return rep

    
    
        
def isempty(linkedList):
    return linkedList.head == None

def size(linkedList):
    return linkedList.size

def size_iterative(linkedList):
    size = 0
    currentNode = linkedList.head 
    while currentNode != None:
        size += 1
        currentNode = currentNode .next
        
    return size


def size_node_recursive(node):
    if node == None:
        return 0
    
    return 1 + size_node_recursive(node.next) ## the size of the rest of the list + 1

def size_recursive(linkedList):
    return size_node_recursive(linkedList.head)



def printLinkedListNonRecursive(linkedList):
    print '<',
    if not isempty(linkedList):
        currentNode = linkedList.head 
        while currentNode != None:
            print currentNode.element, ',',
            currentNode = currentNode .next
    print '>'

            

def printNodeRecursive(node):
    if node == None:
        return
    else:
        print '<',
        print node.element,
        printNodeRecursive(node.next)
        print '>',



def printLinkedListRecursive(linkedList):
    print '<',
    printNodeRecursive(linkedList.head)
    print '>'


def add_first(linkedList, element):
    node = Node(element)
    node.next = linkedList.head
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
        node.next = None
        currentNode.next = node
        linkedList.size += 1



def insert_at(linkedList, element, pos):
    assert linkedList != None, 'Illegal argument None'
    assert pos <= linkedList.size, 'Out-of-bound error'

    if (pos > linkedList.size):
        raise IndexError('list index out of range')
    
    elif pos == 0:
        add_first(linkedList,element)
        
    else:
        currentNode = linkedList.head
        currentIndex = 1
        while currentIndex < pos :
            currentNode = currentNode.next
            currentIndex += 1

        tempPointer = currentNode.next
        newNode = Node(element)
        currentNode.next = newNode
        newNode.next = tempPointer
        linkedList.size += 1
         

def remove_first(linkedList):
    if isempty(linkedList):
        return None
    else:
        first_element = linkedList.head.element
        linkedList.head = linkedList.head.next
        linkedList.size -= 1
        return first_element

def remove_last(linkedList):
    if isempty(linkedList):
        return None
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
        currentNode.next = None
        linkedList.size -= 1
        return tempPointer.element
        

def remove_at(linkedList, pos):
    assert linkedList != None, 'Illegal argument None'
    assert pos <= linkedList.size, 'Out-of-bound error'

    if (pos > linkedList.size):
        raise IndexError('list index out of range')
    
    elif pos == 0:
        return remove_first(linkedList)
        
    else:
        currentNode = linkedList.head
        currentIndex = 1
        while currentIndex < pos :
            currentNode = currentNode.next
            currentIndex += 1

        tempPointer = currentNode.next
        element = tempPointer.element
        currentNode.next = tempPointer.next
        linkedList.size -= 1
         

def reverse(linkedList):
    newList = LinkedList()
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
        
lst = LinkedList()
print 'is empty:', isempty(lst)

add_first(lst, 1)
add_first(lst, 3)
add_first(lst, 4)
add_first(lst, 2)

print '\n print using __repr__:', lst

print '\n print iteratively:',
printLinkedListNonRecursive(lst)

print '\n print recursively:',
printLinkedListRecursive(lst)

insert_at(lst, 10, 0)
insert_at(lst, 30, 5)
add_last(lst, 40)
add_last(lst, 20)

print '\n print using __repr__:', lst

reversed_lst = reverse(lst)

print '\n print iteratively:',
printLinkedListNonRecursive(reversed_lst)

print remove_at(reversed_lst,2)
print remove_last(reversed_lst)
print remove_first(reversed_lst)

print '\n print recursively:',
printLinkedListRecursive(reversed_lst)

print '\n print size using size(...):', size(lst)

print '\n print size using size_recursive(...):', size_recursive(reversed_lst)

print '\n print size using size_iterative(...):', size_iterative(lst)





























































