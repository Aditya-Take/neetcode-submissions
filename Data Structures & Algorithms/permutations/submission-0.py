class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def dfs():
            if len(sol) == len(nums):
                res.append(sol.copy())
            
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    dfs()
                    sol.pop()
        
        dfs()
        return res