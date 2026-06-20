class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}

        for i in range(len(nums)):

            n = nums[i]
            diff = target - n

            if diff in map:
                return [map[diff], i]
            map[n] = i

        return [-1, -1]