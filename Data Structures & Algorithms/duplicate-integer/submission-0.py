class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        if len(nums) == 0:
            return False

        a = []
        a.append(nums[0])

        for i in range(1, len(nums)):
            if nums[i] in a:
                return True
            a.append(nums[i])

        return False