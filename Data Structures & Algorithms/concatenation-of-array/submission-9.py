class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        num = []
        for i in range(2):
            for j in range(len(nums)):
                num.append(nums[j])
            
        return num
        