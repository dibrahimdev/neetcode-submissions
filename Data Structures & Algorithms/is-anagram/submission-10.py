class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        HashMap_1 = {}
        for letter in s:
            if letter not in HashMap_1:
                HashMap_1[letter] = 1
            else:
                HashMap_1[letter] += 1
        HashMap_2 = {}
        for letter in t:
            if letter not in HashMap_2:
                HashMap_2[letter] = 1
            else:
                HashMap_2[letter] += 1
        return HashMap_1 == HashMap_2