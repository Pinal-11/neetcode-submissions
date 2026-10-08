class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}

        for index in range(len(nums)):
            # print("d before:", d)
            req_num = target - nums[index]

            if req_num in d:
                return[d[req_num], index]
            
            d[nums[index]] = index
            # print("d after:", d)