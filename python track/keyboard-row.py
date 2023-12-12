class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans=[]
        first_row="qwertyuiop"
        second_row="asdfghjkl"
        third_row="zxcvbnm"
        temp=""
        

        for i in range(len(words)):
                if words[i][0].lower() in first_row:
                    temp=first_row
                elif words[i][0].lower() in second_row:
                    temp=second_row
                else:
                    temp=third_row
                for j in range(len(words[i])):
                    flag=0
                    if words[i][j].lower() not in temp:
                        flag=1
                        break
                if flag==0:
                    ans.append(words[i])
        return ans
           
                    
                
                
        
                
                    
                

