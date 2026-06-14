class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        freqA = [[] for n in range(len(nums) + 1)]

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        

        for num, freq in freq.items():
            freqA[freq].append(num)
        
        res = []
        for i in range(len(freqA) - 1, 0, -1):
            for s in freqA[i]:
                res.append(s)

                if len(res) == k:
                    return res