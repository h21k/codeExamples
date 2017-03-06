

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


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        rep = '<Queue: size = ' + str(self.size) + ', '
        if self.head != None:
            rep += ', ' + str(self.head)

        rep += '>'
        return rep

    
    
        
def isempty(queue):
    return queue.head == None

def size(queue):
    return queue.size

def enqueue(queue, element):
    node = Node(element)
    if isempty(queue):
        queue.head = node
        queue.tail = node
        queue.size = 1
    else:
        queue.tail.next = node
        queue.tail = node
        queue.size += 1

def dequeue(queue):
    if isempty(queue):
        raise Exception('invalid operation on empty queues.')
    else:
        element = queue.head.element
        queue.head = queue.head.next
        queue.size -= 1
        return element


#######################################################
##
##                TESTS
##
#######################################################
        
queue = Queue()
print 'is empty:', isempty(queue)

print '\n print using __repr__:', queue

enqueue(queue, 1)
print '\n enqueue(queue, 1):', queue

enqueue(queue, 3)
print '\n enqueue(queue, 3):', queue

enqueue(queue, 4)
print '\n enqueue(queue, 4):', queue

print '\n dequeued element is:', dequeue(queue)
print '\n dequeue(queue):', queue

enqueue(queue, 2)
print '\n enqueue(queue, 2)_:', queue












