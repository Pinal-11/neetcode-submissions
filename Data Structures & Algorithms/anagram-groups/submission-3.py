class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping the charCount to list of Anagram

        for s in strs:
            count = [0] * 26 # a....Z

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s) #list cannot be key so converting into the tuple
        # print(res)
        return list(res.values())