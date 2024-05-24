#My Node class
class MyNode:
    def __init__(self,Data,Next):
        self.data = Data
        self.next = Next

    def DisplayNode(self):
        print(self.data)

# My Single Linked List:
class MySSL:
    def __init__(self):
        self.head = None
    def IsEmpty(self):
        if self.head == None:
            return True
        return False
    
    def AddHead(self,NewData):
        NewItem = MyNode(NewData,None)

        if self.IsEmpty():
            self.head = NewItem
        else:
            NewItem.next = self.head
            self.head = NewItem

    def traversalDisplay(self):
        if self.IsEmpty():
            print('queue is empty')
            return
        
        current = self.head
        while current!= None:
            current.DisplayNode()
            current = current.next
    
    def removeHead(self):
        if self.IsEmpty():
            return
        else:
            self.head.next
    

def main():
    print('input')
    mylist = MySSL()
    mylist.AddHead(5)
    mylist.AddHead(4)
    mylist.AddHead(10)
    mylist.AddHead(7)
    print(mylist.traversalDisplay())

if __name__ == "__main__":
    main()