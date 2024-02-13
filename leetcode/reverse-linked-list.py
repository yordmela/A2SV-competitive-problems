# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr=[]
        curr= head
        while curr:
            arr.append(curr.val)
            curr= curr.next
        arr.reverse()
        if arr:
            head= ListNode(arr[0])
        curr=head
        for i in range(1,len(arr)):
            newNode= ListNode(arr[i])
            curr.next= newNode
            curr= curr.next
        return head
        





        