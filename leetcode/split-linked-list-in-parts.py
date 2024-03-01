# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr=head
        length=0
        while curr:
            length+=1
            curr= curr.next
        firstn= length%k
        nextn= length//k
        curr=head
        ans=[]
        while curr:
            if firstn:
                temp=curr
                for i in range(nextn+1):
                    last=curr
                    curr=curr.next
                last.next=None
                firstn-=1
            elif not firstn:
                temp=curr
                for i in range(nextn):
                    last=curr
                    curr=curr.next
                last.next=None
            ans.append(temp)
        while len(ans)<k:
            ans.append(None)
        return ans

