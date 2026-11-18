class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        best=count
        for num in nums:
            if num==1:
                count+=1
            else:
                
                best=max(best,count)
                count=0
        return max(best,count)


        