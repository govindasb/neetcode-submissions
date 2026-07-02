class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sDic = {}
        tDic = {}
        for i in range(len(s)):
            if s[i] in sDic:
                sDic[s[i]]= sDic[s[i]] + 1
            else:
                sDic[s[i]]=1
            if t[i] in tDic:
                tDic[t[i]]= tDic[t[i]] + 1
            else:
                tDic[t[i]]=1
        return sDic == tDic
             
            

        