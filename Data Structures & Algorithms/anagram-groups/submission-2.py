class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for s in strs:

            nums = [0]*26

            for c in s:

                nums[ord(c) - ord('a')] += 1
            
            res[tuple(nums)].append(s)
        
        return list(res.values())