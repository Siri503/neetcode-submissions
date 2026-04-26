from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        sorted_values=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        return [x[0] for x in sorted_values[:k]]
        

        