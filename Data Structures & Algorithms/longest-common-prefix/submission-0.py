class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(len(strs) - 1):
            next_word = strs[i +1]
            for j in range(len(prefix)):
                if j >= len(next_word) or prefix[j] != next_word[j]:
                    prefix = prefix[:j]
                    break
        return prefix