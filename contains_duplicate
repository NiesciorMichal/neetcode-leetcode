class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = False
        for idx, item in enumerate(nums):
            if dups := any(x == item for x in nums[idx+1:]):
                break
        return dups
