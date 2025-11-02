class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""

        for elems in zip(*strs):    # iterates to letters in prefix and val safely
            pre = elems[0]
            keep = False
            retur = False
            for _, val in enumerate(elems):
                if pre != val:
                    keep = False
                    retur = True
                    break
                else:
                    keep = True

            if keep:
                prefix += val
            elif retur:
                return prefix
            
        return prefix
