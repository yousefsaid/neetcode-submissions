class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        seen = {}

        for r in range(len(s2)):
            if s2[r] not in s1:
                seen.clear()
                l = r + 1
                continue
            
            seen[s2[r]] = seen.get(s2[r], 0) + 1

            while r - l + 1 > len(s1):
                seen[s2[l]] -= 1

                if seen[s2[l]] == 0:
                    del seen[s2[l]]
                
                l += 1

            if seen == Counter(s1):
                return True
        
        return False