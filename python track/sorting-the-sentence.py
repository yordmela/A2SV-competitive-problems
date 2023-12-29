class Solution:
    def sortSentence(self, s: str) -> str:
        list1=s.split(" ")
        list1.sort(key=lambda x:x[-1])
        temp=""
        for i in range(len(list1)):
            temp+=list1[i][:len(list1[i])-1]
            temp+=" "
        return temp.strip()
        