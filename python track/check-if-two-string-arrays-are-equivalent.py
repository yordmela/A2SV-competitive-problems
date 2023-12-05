class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
       first_word=""
       second_word=""
       for i in range(len(word1)):
           first_word+=word1[i]
       for i in range(len(word2)):
           second_word+=word2[i]
       if first_word== second_word:
           return True
       return False


           
                
        