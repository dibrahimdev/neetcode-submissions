class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, val in enumerate(nums):
            comp = target - val 
            if comp in nums_dict:
                return [nums_dict[comp], i]
            nums_dict[val] = i
            