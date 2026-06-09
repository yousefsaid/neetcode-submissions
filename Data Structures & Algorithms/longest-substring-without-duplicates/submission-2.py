class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        L = 0
        length = 0


        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[L])
                L += 1
            
            length = max(length, r - L + 1)
            seen.add(s[r])
        return length