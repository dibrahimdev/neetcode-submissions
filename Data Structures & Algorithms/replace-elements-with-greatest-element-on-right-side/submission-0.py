class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                greatest = max(arr[j: ])
                if len(result) < len(arr):
                    result.append(greatest)
            result.append(-1)
            break
        return result