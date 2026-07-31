class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}

        for i in nums:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1

        v = sorted(list(x.values()), reverse=True)[:k]

        a = []

        for freq in v:
            for key, value in x.items():
                if value == freq and key not in a:
                    a.append(key)
                    break

        return a