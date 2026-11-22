class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        newword=""
        newword2=""
        for word in word1:
            newword+=word
        for word in word2:
            newword2+=word
        return newword==newword2

