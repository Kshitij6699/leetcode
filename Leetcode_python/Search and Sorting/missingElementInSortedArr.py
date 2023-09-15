# Input : arr[] = [1, 2, 3, 4, 6, 7, 8]
# Output : 5

class Solution():
    def search(self,nums):
        if nums[0] != 1:
            return 1
        elif nums[len(nums)-1] != len(nums)+1:
            return len(nums)
        
        start = 0
        end = len(nums) - 1

        while(start < end):
            mid = int(start + (end-start)/2)
            if nums[start] - start != nums[mid] - mid:
                end = mid 
            elif nums[end] - end != nums[mid] - mid:
                start = mid 
            return nums[start] + 1

input = [1, 2, 3, 4, 6, 7, 8]
print(Solution().search(input))