class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()
        i = 0
        while i < len(clean) // 2:
            if clean[i] != clean[-i - 1]:
                return False
            i += 1
        return True