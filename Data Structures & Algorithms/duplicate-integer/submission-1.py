class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dicts = {}
        for i in range(len(nums)-1):
            dicts[nums[i]] = dicts.get(nums[i],0)
            if nums[i+1] in dicts:
                return True
        # print(dicts)         
        return False