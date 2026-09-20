class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       table = set()
       for number in nums:
        if number in table:
            return True
        else:
            table.add(number)
       return False