class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify numss in-place instead.
        """
        
        left=0
        right=1
        
        while(right<=len(nums)-1 and left<=len(nums)-1):
            if left>right:
                right=right+1
            if nums[left]==0:
                if nums[right]!=0:
                    nums[left],nums[right]=nums[right],nums[left]
                    right=right+1
                else:
                    right=right+1
            else:
                left=left+1
