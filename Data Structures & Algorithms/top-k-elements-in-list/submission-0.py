class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:

            if n in num_freq:
                num_freq[n] += 1
            else:
                num_freq[n] = 1
        
        for n, c in num_freq.items():
            freq[c].append(n)
        

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
