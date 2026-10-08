class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        res_list = []
        nums_count = {}

        for index in range(len(nums)):
            nums_count[nums[index]] = nums_count.get(nums[index], 0) + 1
            # if nums_count[nums[index]] == k :
            #     res_list.append(nums[index])
        
        # print(nums_count)
        # nums_list = nums_count.values()
        # nums_list = sorted(nums_list)
        # print(nums_list)

        for key, val in nums_count.items():
            res_list.append([val, key])
        res_list.sort()
        
        for index in range(len(res_list)-1, len(res_list)-k-1, -1):
            res.append(res_list[index][1])

        # print(f"res_list {res_list}")
        # print(f"res {res}")
        
        return res
        