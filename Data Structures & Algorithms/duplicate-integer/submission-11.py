class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        HashMap = {}
        for num in nums:
            if num not in HashMap:
                HashMap[num] = 1
            else:
                HashMap[num] += 1
        for val in HashMap.values():
            if val > 1:
                return True
        return False
        