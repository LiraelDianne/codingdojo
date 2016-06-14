class Node(object):
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def addNode(self, node):
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

    def insertNode(self, node, next):
        if next.prev:
            next.prev.next = node
            node.prev = next.prev
        else:
            self.head = node
        node.next = next
        next.prev = node

    def deleteNode(self, node):
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

    def printVals(self):
        if self.head:
            print "List:"
            print self.head.name
            if self.tail is not self.head:
                current = self.head.next
                while current is not self.tail:
                    print current.name
                    current = current.next
                print self.tail.name
        else:
            print "Empty list"

alice = Node('alice')
bob = Node('bob')
carol = Node('carol')

people = DoublyLinkedList()
people.printVals()
people.addNode(carol)
people.printVals()
people.insertNode(alice, carol)
people.printVals()
people.insertNode(bob, carol)
people.printVals()
people.deleteNode(bob)
people.printVals()
people.deleteNode(carol)
people.printVals()
people.deleteNode(alice)
people.printVals()
