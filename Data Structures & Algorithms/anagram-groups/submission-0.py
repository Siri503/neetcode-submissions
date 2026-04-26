class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for w in strs:
            k=' '.join(sorted(w))
            if k not in dic:
                dic[k]=[]
            dic[k].append(w)
        return list(dic.values())
        