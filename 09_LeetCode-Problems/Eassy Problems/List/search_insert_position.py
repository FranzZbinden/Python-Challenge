class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        min = 0
        max = len(nums) -1  # -1 for real index 

        while min <= max:
            mid = (min + max) // 2      # update mid
            if nums[mid] == target:     # found    
                return mid          
            elif nums[mid] > target:    # target smaller than mid
                max = mid - 1               # Adjust max & discard already checked index-val
            elif nums[mid] < target:    # target larger than mid
                min = mid + 1               # Adjust min & discard already checked index-val
            
        return min                      # return place to be