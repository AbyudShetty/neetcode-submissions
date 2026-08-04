class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        a = sorted(set(nums))
        count = 1;
        counts = []
        if len(a) == 0:
            return 0
        if len(a) == 1:
            return 1
        for i in range(len(a)-1):
            if a[i] == a[i+1] - 1:
                count = count + 1
            else:
                counts.append(count)
                count = 1;
        counts.append(count)
        return max(counts)
        