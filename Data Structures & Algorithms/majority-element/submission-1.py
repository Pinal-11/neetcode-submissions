class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        element_dict = {}

        for index in range(len(nums)):
            element_dict[nums[index]] = element_dict.get(nums[index], 0) + 1
        
        
        max_val = max(element_dict.values())

        for key, val in element_dict.items():
            if max_val == element_dict[key]:
                return key

        