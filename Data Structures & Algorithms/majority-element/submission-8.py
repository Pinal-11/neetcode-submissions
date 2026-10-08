class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # nums.sort()
        # return nums[len(nums)//2]

        element_dict, n = {}, len(nums)
        for index in range(n):
            element_dict[nums[index]] = element_dict.get(nums[index], 0) + 1
            if element_dict[nums[index]] > n//2:
                return nums[index]
        
        # max_val = max(element_dict.values())
        # for key, val in element_dict.items():
        #     if max_val == val:
        #         return key

        