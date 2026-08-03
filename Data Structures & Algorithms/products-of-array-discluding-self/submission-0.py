class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            n = nums.copy()
            n.pop(i)
            a.append(math.prod(n))
        return a
        