class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        start = 1
        for time in range(2):
            for num in nums:
                ans.append(num)
        return ans

