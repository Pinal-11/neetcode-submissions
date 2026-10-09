class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # store_list = [[0]] * 26
        element_dict = {}

            
        for ch in strs:
            temp_tuple = tuple(sorted(ch))
            if temp_tuple in element_dict:
                element_dict[temp_tuple].append(ch)
            else:
                element_dict[temp_tuple] = [ch]
        # print(element_dict)

        return list(element_dict.values())
