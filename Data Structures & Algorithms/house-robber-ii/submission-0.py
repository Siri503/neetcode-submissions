from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        def robber(x: List[int]) -> int:
            m = len(x)
            if m == 0:
                return 0
            if m == 1:
                return x[0]
            if m == 2:
                return max(x[0], x[1])
            
            dp = [0] * m
            dp[0] = x[0]
            dp[1] = max(x[0], x[1])
            for i in range(2, m):
                dp[i] = max(dp[i - 1], dp[i - 2] + x[i])
            return dp[m - 1]
        return max(robber(nums[:-1]), robber(nums[1:]))

