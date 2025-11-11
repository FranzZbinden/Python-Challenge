class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ""
        # lst -> string 
        for val in digits:
            st += str(val)

        num_i = int(st) # <- converts to int to + 1
        num_i += 1
        num_s = str(num_i) # <- # needs to be on string to iterate char to char
        lst = []  # <- creates list to return

        # iterates on string -> lst:int
        for idx in range(len(num_s)):
            lst.append(int(num_s[idx]))
        return lst