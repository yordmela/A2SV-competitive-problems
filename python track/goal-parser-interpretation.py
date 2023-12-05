class Solution:
    def interpret(self, command: str) -> str:
        p=0
        ans=""
        while p<len(command):
            if command[p]=="G":
                ans+="G"
            elif command[p]=="(" and command[p+1]==")":
                ans+="o"
                p+=1
            elif command[p]=="(" and command[p+1]=="a":
                ans+="al"
                p+=3
            else:
                p+=1
            p+=1
        return ans

        