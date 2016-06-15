class Node(object):
    def __init__(self, value):
        self.val = value
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        node = Node(value)
        if self.head:
            if self.tail.prev:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                self.tail = node
                self.head.next = node
                self.tail.prev = self.head
        else:
            self.head = node
            self.tail = node
        return self

    def insertNode(self, value, beforeval):
        node = Node(value)
        next = self.head
        while next and next.val != beforeval:
            if next.next:
                next = next.next
            else:
                print "value not in list"
                return self
        if next.prev:
            next.prev.next = node
            node.prev = next.prev
        else:
            self.head = node
        node.next = next
        next.prev = node
        return self

    def deleteNode(self, value):
        node = self.head
        while node and node.val != value:
            if node.next:
                node = node.next
            else:
                print "value not in list"
                return self
        if node.prev:
            if node.next:
                node.prev.next = node.next
                node.next.prev = node.prev
            else:
                self.tail = node.prev
                node.prev.next = None
        else:
            if node.next:
                self.head = node.next
                node.next.prev = None
            else:
                self.head = None
                self.tail = None
        node.prev = None
        node.next = None
        return self

    def printVals(self):
        if self.head:
            print "List:"
            print self.head.val
            if self.tail is not self.head:
                current = self.head.next
                while current is not self.tail:
                    print current.val
                    current = current.next
                print self.tail.val
        else:
            print "Empty list"
        return self

people = DoublyLinkedList()
people.printVals()

people.addNode('carol').printVals()

people.insertNode('alice', 'carol').printVals()

people.insertNode('bob', 'carol').printVals()

people.deleteNode('bob').printVals()

people.deleteNode('carol').printVals()

people.deleteNode('alice').printVals()
