class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans = nums * 2
        # print(ans)
        #----------------
        # for i in range(len(nums)):
        #     nums.append(nums[i])
        # return nums
        #-----------
        nums.extend(nums)
        return nums