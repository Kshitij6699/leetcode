class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList(Node):
    def __init__(self):
        self.head = None

    def printLL(self):
        temp = self.head
        while(temp != None):
            print(temp.data,end="->")
            temp = temp.next
        print("None")

    def lengthLL(self):
        temp = self.head
        count = 0
        while (temp != None):
            count += 1
            temp = temp.next
        return count
    
    def insertInHead(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    def insertAtEnd(self,data):
        newNode = Node(data)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode
    
    def insertAtPos(self,data,pos):
        if pos < 0:
            print("Invalid Position requested,data cannot be inserted.")
            return self.head
        if pos == 0 or pos == 1:
            return LinkedList.insertInHead(data,pos)
        len = LinkedList.lengthLL(self)
        if pos > len:
            return LinkedList.insertInEnd(data,pos)
        prev = None
        curr = self.head
        while pos != 1:
            pos -= 1
            prev = curr
            curr = curr.next
        newNode = Node(data)
        prev.next = newNode
        newNode.next = curr.next
        del curr
    
    def deleteAtHead(self):
        if self.head is None:
            print('Null LinkedList')
            return self.head
        if self.head.next is None:
            return None
        
