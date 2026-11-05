class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = {}
        for letter in s:
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
        for t_letter in t:
            if t_letter in count:
                count[t_letter] -= 1
            else:
                return False
        for value in count.values():
            if value != 0:
                return False
        return True

               