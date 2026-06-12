class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqS = {}
        freq = [[] for n in range(len(nums) + 1)]

        for n in nums:

            freqS[n] = freqS.get(n, 0) + 1

        for i, n in freqS.items():
            freq[n].append(i)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res