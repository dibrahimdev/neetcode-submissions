class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans_dict = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in ans_dict:
                return [ans_dict[complement], i]
            ans_dict[val] = i
        return []
