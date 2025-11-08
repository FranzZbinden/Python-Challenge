
#    not efficient at all... vvvvvvvvvvvvvv
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        for idx, val in enumerate(nums[:]):
            if val not in seen.values():
                seen[idx] = val
            elif val in seen.values():
                nums.remove(val)
                
        return len(nums)


# Wayyy more efficient vvvvvvvvvvvvvvv
# do not use [.values()], [remove()] or [dictionaries] 
class Solution:
    def removeDuplicates(self, nums):
        if not nums:    # handle edge case 
            return 0

        unique_num = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[unique_num]:
                nums[unique_num+1] = nums[i]
                unique_num+= 1

        return unique_num + 1



