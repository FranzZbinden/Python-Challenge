class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        for i in range(1, len(nums)):

            if nums[i] == nums[i-1]:
            
                left = nums[:i]
                right = nums[i+1:]
                nums = left + right



        return len(nums) 



        