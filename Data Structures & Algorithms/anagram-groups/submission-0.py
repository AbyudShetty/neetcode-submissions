class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        if len(strs) == 0:
            return [[""]]
        for x in strs:
            y = "".join(sorted(x))
            if y in groups:
                z = groups[y]
                z.append(x)
            else:
                groups[y] = [x]
        return list(groups.values())