# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy= ListNode()
        dummy.next= head
        Lprev= dummy
        curr= dummy.next
        # reach the left most node
        for i in range(left-1):
            Lprev= Lprev.next
            curr= curr.next

        # reverse the next of every node within(left,right)
        prev=None
        for i in range(right-left+1):
            temp= curr.next
            curr.next= prev
            prev= curr
            curr= temp
        Lprev.next.next=curr
        Lprev.next= prev
        return dummy.next

        
        