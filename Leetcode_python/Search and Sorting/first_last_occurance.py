# link: -https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]

class Solution:
    def first_occurrence(self,nums,target):
        start = 0
        end = len(nums) - 1
        ans = -1
        while(start <= end):
            mid = int(start + (end - start)/2)
            if nums[mid] == target:
                ans = mid
                if nums[mid] == nums[mid-1]:
                    end = mid - 1
                else:
                    return ans
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return ans
    
    def last_occurrence(self, nums,target):
        start = 0
        end = len(nums) - 1
        ans = -1

        while(start <= end):
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        return ans

    def searchRange(self, nums, target):
        first_occ = Solution().first_occurrence(nums,target)
        last_occ = Solution().last_occurrence(nums,target)
        lst =[]
        lst.append(first_occ)
        lst.append(last_occ)
        return lst 

input = [5,7,7,8,8,10]
target = 8
#print(Solution().first_occurrence(input,target))
#print(Solution().last_occurrence(input,target))
print(Solution().searchRange(input,target))    