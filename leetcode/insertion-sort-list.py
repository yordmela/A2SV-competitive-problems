# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next==None:
            return head
        dummy=ListNode(float('-inf'))
        dummy.next=head
        
        prev= dummy.next
        curr= prev.next
        while prev and curr:
            
            if curr.val>=prev.val:
                curr=curr.next
                prev=prev.next
            else:
                temp=curr
                prev.next= curr.next
                curr=dummy
                while curr and temp.val>curr.next.val:
                    curr= curr.next
                    
                temp.next=curr.next
                curr.next=temp
                
                if prev:
                    curr=prev.next
        return dummy.next