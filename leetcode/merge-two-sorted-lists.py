# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        curr1= list1
        curr2= list2
        if (curr1 and curr2 and curr1.val< curr2.val) or (not curr2 and curr1):
            dummy.next= curr1
            curr1= curr1.next
        elif (curr1 and curr2) or(not curr1 and curr2):
            dummy.next= curr2
            curr2= curr2.next
        curr= dummy.next
        
        while curr1 and curr2 and curr:
            if curr1 and curr2 and curr1.val< curr2.val:
                curr.next= curr1
                curr1= curr1.next
            else:
                curr.next= curr2
                curr2= curr2.next
            curr= curr.next
        if curr1 and curr:
            curr.next= curr1
        if curr2 and  curr:
            curr.next= curr2
        return dummy.next

    