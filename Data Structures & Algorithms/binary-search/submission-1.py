class Solution:
    def search(self, nums: List[int], target: int) -> int:
        sort=nums
        lo=0
        hi=len(sort)-1
        mid=round(hi/2)
        while(lo<=hi):
            if sort[mid]==target:
                return mid
            else:
                if target<sort[mid]:
                    hi=mid-1
                    mid=round((lo+hi)/2)
                else:
                    lo=mid+1
                    mid=round((lo+hi)/2)
        return -1

