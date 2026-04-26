class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p=nums[0]
        min_p=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            temp_mx=max_p
            num=nums[i]
            max_p=max(num,max_p*num,min_p*num)
            min_p=min(num,temp_mx*num,min_p*num)
            ans=max(ans,max_p)
        return ans