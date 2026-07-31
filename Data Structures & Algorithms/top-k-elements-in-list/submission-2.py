from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = Counter(nums)

        a = []

        for key, value in x.most_common(k):
            a.append(key)

        return a