class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l={}
        for i in range(len(nums)):
            if nums[i] in l:
                l[nums[i]]+=1
            else:
                l[nums[i]]=1
        for i,j in l.items():
            if j==1:
                return i
            # print(j)
                
        