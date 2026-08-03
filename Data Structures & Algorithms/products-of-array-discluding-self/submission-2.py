class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)): 
            x = nums[i]
            nums[i] = 1
            a.append(math.prod(nums))
            nums[i] = x
        return a
        