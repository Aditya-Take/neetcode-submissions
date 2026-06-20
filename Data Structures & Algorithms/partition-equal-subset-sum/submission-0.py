class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)


        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        amount = total_sum //2

        dp = [False] * (amount + 1)
        dp[0] = True

        for num in nums:
            for cost in range(amount, num-1, -1):
                if dp[cost-num]:
                    dp[cost] = True
        
        return dp[amount]