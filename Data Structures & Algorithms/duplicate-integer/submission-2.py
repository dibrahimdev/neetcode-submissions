class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        checked = []
        result = True
        for num in nums:
            if num not in checked:
                checked.append(num)
            if len(checked) == len(nums):
                result = False
        return result