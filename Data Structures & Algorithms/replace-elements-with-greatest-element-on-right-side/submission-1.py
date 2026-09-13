class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr) - 1):
            greatest = max(arr[i + 1: ])
            if len(result) < len(arr) - 1:
                result.append(greatest)
        result.append(-1)
        return result