class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dp=[0]*26
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            dp[ord(s[i])-ord('a')]+=1
            dp[ord(t[i])-ord('a')]-=1
        for c in dp:
            if c!=0:
                return False
        return True
        