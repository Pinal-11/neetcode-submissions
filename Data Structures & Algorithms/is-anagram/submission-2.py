class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}

        if len(s) == len(t):
            for ch in range(len(s)):
                sdict[s[ch]] = sdict.get(s[ch], 0) + 1
                tdict[t[ch]] = tdict.get(t[ch], 0) + 1
            if sdict == tdict:
                return True

        # print(sdict)
        # print(tdict)
        return False
        