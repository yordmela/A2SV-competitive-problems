# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd= head
        if not odd:
            return head
        even= odd.next
        even_head= even
        # make the curr odd point to the next odd and the curr even point to the next even
        while odd and odd.next and even and even.next :
            odd.next= odd.next.next
            even.next= even.next.next
            odd= odd.next
            even= even.next
        odd.next= even_head
        return head