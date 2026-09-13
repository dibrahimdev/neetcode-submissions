class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        result = [] + nums_copy + nums
        return result        
        