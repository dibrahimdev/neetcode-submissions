class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}
        for index, val in enumerate(nums):
            comp = target - val
            if comp in count:
                return [count[comp], index]
            count[val] = index
            