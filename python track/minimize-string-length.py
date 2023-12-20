class Solution:
    def minimizedStringLength(self, s: str) -> int:
        hashSet=set()
        for i in range (len(s)):
            hashSet.add(s[i])
        return len(hashSet)