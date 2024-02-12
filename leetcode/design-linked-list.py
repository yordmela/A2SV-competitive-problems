class Node:
    def __init__(self,val,next):
        self.val=val
        self.next=next
class MyLinkedList:

    def __init__(self):
        self.head=None
       

    def get(self, index: int) -> int:
        curr=self.head
        while index>0 and curr:
            curr= curr.next
            index-=1
        if curr:
            return curr.val
        return -1
        


    def addAtHead(self, val: int) -> None:
        newNode= Node(val,self.head)
        self.head= newNode
        

    def addAtTail(self, val: int) -> None:
        newNode=Node(val,None)
        prev=self.head
        while prev and prev.next:
            prev= prev.next
        if prev:
            prev.next=newNode
        else:
            self.head= newNode
        newNode.next= None
        
    
        

    def addAtIndex(self, index: int, val: int) -> None:
        dummy= Node(1,None)
        dummy.next=self.head
        newNode=Node(val,None)
        prev= dummy
        while index and prev and prev.next:
            prev= prev.next
            index-=1
        if prev and not index:
            newNode.next=prev.next
            prev.next= newNode
        self.head= dummy.next
        
        


        
        

    def deleteAtIndex(self, index: int) -> None:
        dummy= Node(1, None)
        dummy.next= self.head
        prev=dummy
        while index and prev and prev.next:
            prev= prev.next
            index-=1
        if prev and prev.next:
            prev.next= prev.next.next
        self.head= dummy.next
        

        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)