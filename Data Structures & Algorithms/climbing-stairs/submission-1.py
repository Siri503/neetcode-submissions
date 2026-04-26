class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        p2=1
        p1=1
        for i in range(2,n+1):
            cu=p1+p2
            p2=p1
            p1=cu
        return p1
        