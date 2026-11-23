class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        sort=[]
        while (left<=right):
            if abs(nums[left])<abs(nums[right]):
                sort.append((nums[right])**2)
                right-=1
            else:
                
                sort.append((nums[left])**2)
                left+=1
        return sort[::-1]
            