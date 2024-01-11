class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        l,r=0,0
        dic=defaultdict(int)
        minimum=len(cards)
        flag=False
        while r<len(cards):

            while cards[r] in dic:
                flag=True
                minimum= min(minimum, r-l+1)
                dic[cards[l]]-=1
                if dic[cards[l]]==0:
                    dic.pop(cards[l])
                l+=1
            dic[cards[r]]+=1
            r+=1
        if flag==False:
            return -1
        return minimum
        