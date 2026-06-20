class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, subset = [], []
        
        n = len(nums)
        def dfs(i):
            if i == n:
                res.append(subset.copy())
                return
            
            #don't pick
            dfs(i + 1)

            #pick
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()
        
        dfs(0)

        return res