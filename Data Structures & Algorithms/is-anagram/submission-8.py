class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_dict = {}
        for letter in s:
            if letter in word_dict:
                word_dict[letter] += 1
            else:
                word_dict[letter] = 1
        for letter in t:
            if letter in word_dict:
                word_dict[letter] -= 1

        for val in word_dict.values():
            if val != 0:
                return False
        return True