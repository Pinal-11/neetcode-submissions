class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res_dict = {}

        for index in range(len(nums)):
            temp_num = target - nums[index]

            if temp_num in res_dict:
                return[res_dict[temp_num], index]
            
            res_dict[nums[index]] = index