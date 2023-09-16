# link :- https://practice.geeksforgeeks.org/problems/first-repeating-element4018/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# arr[] = {1, 5, 3, 4, 3, 5, 6}
# Output: 2
# Explanation: # 5 is appearing twice and its first appearence is at index 2  which is less than 3 whose first
# occuring index is 3. 

class Solution:
    #Function to return the position of the first repeating element.
    def firstRepeated(self,arr, n):
        max_ = max(arr)
        
        hash = [0] * (max_ + 1)

        for i in range(n):
            hash[arr[i]] += 1

        repeating  = float('inf')

        for i in range(n):
            if hash[arr[i]] > 1:
                repeating = i
                break
        if repeating  == float('inf'): return -1
        else: return repeating+1

Input = [1, 5, 3, 4, 3, 5, 6]
n =len(Input)
print(Solution().firstRepeated(Input,n))
