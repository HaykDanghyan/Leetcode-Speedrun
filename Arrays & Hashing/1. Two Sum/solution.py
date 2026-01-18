from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # t/c: O(n), s/c: O(n)

        dct = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in dct:
                return [i, dct[find]]
            else:
                dct[nums[i]] = i
        
        return [-1, -1]