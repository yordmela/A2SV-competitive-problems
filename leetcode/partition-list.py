# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1= ListNode()
        dummy2=ListNode()
        small= dummy1
        large= dummy2
        curr=head
        while curr :
            if curr.val<x:
                small.next= curr
                small= small.next
            else:
                large.next= curr
                large= large.next
            curr= curr.next
        small.next=dummy2.next
        large.next= None
        return dummy1.next