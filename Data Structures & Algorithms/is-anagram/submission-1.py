class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sdict = {}
        tdict = {}

        for index in range(len(s)):
            sdict[s[index]] = sdict.get(s[index],0)+1
            tdict[t[index]] = tdict.get(t[index],0)+1

        if sdict == tdict:
            return True
        else:
            return False