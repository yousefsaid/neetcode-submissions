class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numList = defaultdict(int)
        maxCount = res = 0

        for num in nums:
            numList[num] += 1

            if numList[num] > maxCount:
                res = num
                maxCount = numList[num]
        
        return res