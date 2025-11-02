class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleNum = 0
        for i in range(len(nums)):
            singleNum ^= nums[i] # Use of XOR operator to be left with the single number on the list

        return singleNum

        