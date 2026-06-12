class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}

        for i, n in enumerate(nums):
            second = target - n

            if second in seen:
                return [seen[second], i]
            else:
                seen[n] = i