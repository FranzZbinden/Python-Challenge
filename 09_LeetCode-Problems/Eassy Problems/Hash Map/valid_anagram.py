class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letter_s = {}
        letter_t = {}

        for idx in range(len(s)):
            letter_s[s[idx]] = letter_s.get(s[idx],0) + 1 

        for idx in range(len(t)):
            letter_t[t[idx]] = letter_t.get(t[idx],0) + 1

        if len(s) == len(t):
            for idx in range(len(s)):
                if letter_s[s[idx]] != letter_t.get(s[idx],0):
                    return False
        else:
            return False
        
        return True
