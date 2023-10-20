# Link:- https://practice.geeksforgeeks.org/problems/key-pair5616/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
# Input:
# N = 6, X = 16
# Arr[] = {1, 4, 45, 6, 10, 8}
# Output: Yes
# Explanation: Arr[3] + Arr[4] = 6 + 10 = 16

# T.C = O(nLog(n))
class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		# code here
		arr.sort()
		i , j = 0, len(arr) -1 
		while(i<j):
			if arr[i] + arr[j] == x:
				return True
			elif arr[i] + arr[j] > x:
				j -= 1
		    else:
				i += 1
		return False

#T.C = O(n), using hashing
