class Solution:
    def decodeString(self, s: str) -> str:
        def decode(s, fq, indx):
            freq=""
            string=""
            index=indx
            while index<len(s):
                if s[index].isdigit():
                    freq+=s[index]
                elif s[index].isalpha():
                    string+=s[index]
                elif s[index]=="[":
                    strs= decode(s, freq, index+1)
                    freq=""
                    string+= strs[0]
                    index = strs[1]
                elif s[index]=="]":
                    return [int(fq) * string,index]
                index+=1
            return [int(fq) * string,index]
            
        return decode(s, 1, 0)[0]