class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        sdict = {}
        tdict = {}

        for ch in s:
            sdict[ch] = sdict.get(ch, 0) + 1
        print(sdict)

        for ch in t:
            tdict[ch] = tdict.get(ch, 0) + 1
        print(tdict)

        if sdict == tdict:
            return True
        else:
            return False
        