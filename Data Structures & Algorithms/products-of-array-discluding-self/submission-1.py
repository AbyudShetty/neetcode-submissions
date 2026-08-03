class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = []
        for i in range(len(nums)):
            x = nums.pop(i)
            a.append(math.prod(nums))
            nums.insert(i,x)
        return a
        