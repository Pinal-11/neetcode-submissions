class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        res = 0 # len(nums) - n(val)

        result_list = []

        for index in range(len(nums)):
            if val != nums[index]:
                result_list.append(nums[index])
        nums.clear()
        nums.extend(result_list)
        # print(result_list)
        return len(nums)
