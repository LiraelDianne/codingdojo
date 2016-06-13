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
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail = node
            if not self.tail.prev:
                self.head.next = node
            else:
                self.tail.prev = node

    def insertNode(self, node, prev, next):
        node.next = next
        node.prev = prev
        node.prev.next = node
        node.next.prev = node

    def deleteNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def printVals(self):
        if self.head:
            print head.name
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
people.addNode(alice)
people.printVals()
people.addNode(carol)
people.printVals()
people.insertNode(bob, alice, carol)
people.printVals()
people.deleteNode(carol)
people.printVals()
