# Given a string s, return true if it is a palindrome, otherwise return false.
# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.
# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# Example 1:
# Input: s = "Was it a car or a cat I saw?"
# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:
# Input: s = "tab a cat"
# Output: false
# Explanation: "tabacat" is not a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_no_ws = "".join(ch.lower() for ch in s if ch.isalnum()) # join everything into a string except spaces and symbols

        rgt = len(s_no_ws) -1
        lft = 0
        
        while lft < rgt:    # until intersection, check if equal
            if s_no_ws[lft] == s_no_ws[rgt]:
                lft += 1    
                rgt -= 1 
            else: 
                return False # not palindrome
        
        return True # palindrome
    
