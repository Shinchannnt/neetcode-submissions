class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left=0
        right=1
        l=len(nums)-1
        k=0
        while(left<=l and right<=l and left<right):
            if nums[left]==nums[right]:
                right=right+1
            else:
                left=left+1
                nums[left]=nums[right]
                k=k+1
                right=right+1
        return k+1
                
               
      
            

        