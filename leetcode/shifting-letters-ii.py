class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix_sum= [0]*len(s)
        def findPrefix(arr):
            accu=0
            new=[0]*len(arr)
            for i in range(len(arr)):
                accu+=arr[i]
                new[i]=accu
            return new
        for shift in shifts:
            if shift[-1]==0:
                prefix_sum[shift[0]]-=1
                if shift[1]!=len(prefix_sum)-1:
                    prefix_sum[shift[1]+1]+=1
            else:
                prefix_sum[shift[0]]+=1
                if shift[1]!=len(prefix_sum)-1:
                    prefix_sum[shift[1]+1]-=1
        
        
        change= findPrefix(prefix_sum)
        print(change)
        ans=""
        for i in range (len(s)):
            ans += chr(((ord(s[i])+change[i]-97)%26)+97)
        return ans
        