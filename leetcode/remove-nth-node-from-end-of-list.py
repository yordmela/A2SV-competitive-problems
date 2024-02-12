# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode= ListNode()
        dummyNode.next= head
        forward=dummyNode
        slow=dummyNode
        while n:
            n -= 1
            forward=forward.next
        while forward.next:
            forward= forward.next
            slow= slow.next
        slow.next= slow.next.next
        return dummyNode.next

        

            
        