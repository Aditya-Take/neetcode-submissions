class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {1 : 1, 2 : 2}

        if n in memo:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-2) + self.climbStairs(n-1)
            return memo[n]
        
    