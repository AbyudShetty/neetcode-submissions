class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = list(s)
        b = list(t)

        if sorted(a) == sorted(b):
            return True
        return False