# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

# Example 5:
# Input: s = "([)]"
# Output: false

class Solution:
    def isValid(self, s: str) -> bool:
        prth = {')':'(',
                '}':'{', 
                ']':'['}
        prth_lst = []

        for curr in s:
            if curr in prth:
                if prth_lst and prth_lst[-1] == prth[curr]: # check if stack has top opening prth corresponding to closing prth(curr)
                    prth_lst.pop() # close parenthesis
                else: 
                    return False # empty or no match 
            else:
                prth_lst.append(curr)   # add opening prth

        return True if not prth_lst else False
               