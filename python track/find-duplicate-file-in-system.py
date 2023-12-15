class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic={}
        for path in paths:
            singlePath= path.split(" ")
            directory=singlePath[0]
            for message in range(1, len(singlePath)):
                start=singlePath[message].index("(")
                end=singlePath[message].index(")")
                content= singlePath[message][start+1:end]
                fileName= singlePath[message][:start]
                fullPath= directory+"/"+fileName
                if content in dic:
                    dic[content].append(fullPath)
                else:
                    dic[content]=[fullPath]
        ans = [group for group in dic.values() if len(group) > 1]
        return ans