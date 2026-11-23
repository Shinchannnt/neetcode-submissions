class Solution:
    def makeGood(self, s: str) -> str:
        stack=[]
        string=""
        for letters in s:
            if stack==[]:
                stack.append(letters)
            elif (letters.lower() == stack[-1] or letters.upper()==stack[-1]) and letters!=stack[-1]:
                stack.pop(-1)
            else:
                stack.append(letters)
        for letter in stack:
            string=string+letter
        return string

        


