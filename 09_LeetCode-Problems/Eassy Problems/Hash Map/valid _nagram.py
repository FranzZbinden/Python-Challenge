class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) is not len(t):
            return False
        
        s_ = {}
        t_ = {}

        for idx in range(len(t)):
            s_[s[idx]] = s_.get(s[idx], 0) + 1
            t_[t[idx]] = t_.get(t[idx], 0) + 1

        for i in range(len(t)):
            if s_[i] != t_.get(i,0): 
                return False

        return True