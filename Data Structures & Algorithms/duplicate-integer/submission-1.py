class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False

        a = set(nums)

        if len(nums) == len(a):
            return False
        else:
            return True