class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        def custom_key(words):
                return [order.index(char) for char in words]
        new_words= sorted(words, key=custom_key)
        if new_words== words:
            return True
        return False

