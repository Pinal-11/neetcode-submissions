class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        res_list = [1]
        res_list2 = [1]
        res = []
        prefix = 1

        for index in range(0, len(nums)-1):
            prefix *= nums[index]
            res_list.append(prefix)

        # print("res_list", res_list)
        postfix = 1
        for index in range(len(nums)-1, 0, -1):
            postfix *= nums[index]
            res_list2.append(postfix)
        # print("res_list2: ", res_list2)

        for index in range(len(res_list)):
            res_list[index]*=res_list2[len(res_list)-index-1]

        

        return res_list