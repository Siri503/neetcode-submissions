class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        
        if n==0:
            return 0
        if n==1:
            return nums[0]

        ans1=self.robo(nums[1:])
        ans2=self.robo(nums[:-1])
        return max(ans1,ans2)

    def robo(self,num):
        if len(num)==1:
            return num[0]
        dp=[0]*len(num)
        dp[0]=num[0]
        dp[1]=max(num[0],num[1])
        for i in range(2,len(num)):
            dp[i]=max(dp[i-1],dp[i-2]+num[i])
        return dp[-1]
    