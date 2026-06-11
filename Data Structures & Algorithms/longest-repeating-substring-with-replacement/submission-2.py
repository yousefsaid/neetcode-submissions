class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, count, maxS, res = 0, {}, 0, 0


        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1

            maxS = max(maxS, count[s[r]])


            while (r - l + 1 - maxS) > k:
                count[s[l]] -= 1
                if count[s[l]] == 0:
                    del count[s[l]]
                l += 1
            
            res = max(res, r - l + 1)
        return res