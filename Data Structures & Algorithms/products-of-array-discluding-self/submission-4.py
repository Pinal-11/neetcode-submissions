class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_list = [1] * len(nums)
        prefix = 1
        postfix = 1
        for index in range(len(nums)):
            res_list[index] *= prefix
            prefix *= nums[index]
            # print("res_list: ", res_list)
            res_list[len(nums)-1-index] *= postfix
            postfix *= nums[len(nums)-1-index]
            # print("res_list: ", res_list)

        return res_list