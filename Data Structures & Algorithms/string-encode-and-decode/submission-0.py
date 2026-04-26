class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+"#"+i
        return res

    def decode(self, s: str) -> List[str]:
        l=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!="#":
                j+=1
            le=int(s[i:j])
            l.append(s[j+1:j+1+le])
            i=j+1+le
        return l



