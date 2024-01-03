class Solution(object):
       def dividePlayers(self, skill):
            l,r= 0, len(skill)-1
            res=0
            skill.sort()
            eachPlayer= sum(skill)/ (len(skill)/2)
            while l<r:
                if skill[l]+skill[r]==eachPlayer:
                    res+= skill[l]*skill[r]
                    l+=1
                    r-=1
                else:
                    return -1
            return res
                                
                        
                
                        
