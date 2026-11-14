class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            
            if char=='[' or char=='{' or char=='(':
                stack.append(char)
            else:
                if char=='}':
                    corr='{'
                elif char==']':
                    corr='['
                else:
                    corr='('
                if not stack or stack[-1]!=corr :
                    return False
                stack.pop()
        return len(stack)==0

        

        