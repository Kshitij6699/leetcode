# Array = {1, 2, 2, 4}
# Output: 1 2 4

class Solution:	
	def remove_duplicate(self, lst):
        i = 0
        N = len(lst)
        for j in range(1,N):
            if lst[i] != lst[j]:
                i+=1
                lst[i] = lst[j]
                
        return i+1

input = [1,2,2,4]
print(Solution().remove_duplicate(input))