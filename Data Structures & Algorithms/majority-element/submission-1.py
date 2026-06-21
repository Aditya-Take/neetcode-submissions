class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = 1
        res = nums[0]

        for n in nums: 
            
            if counter == 0:
                res = n
            counter += (1 if n == res else -1)
        
        return res