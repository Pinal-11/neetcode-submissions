class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_list = [1]
        prefix = 1
        for index in range(0, len(nums)-1):
            prefix *= nums[index]
            res_list.append(prefix)

        postfix = 1
        for index in range(len(nums)-1, -1, -1):
            res_list[index] *= postfix
            postfix *= nums[index]

        return res_list