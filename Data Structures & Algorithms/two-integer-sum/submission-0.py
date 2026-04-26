class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for i in range(len(nums)):
            com=target-nums[i]
            if com in dict:
                return [dict[com],i]
            dict[nums[i]]=i
        
        