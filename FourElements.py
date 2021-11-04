'''
Four Elements
Given an array A of N integers. You have to find whether a combination of four elements in the array whose sum is equal to a given value X exists or not.
 

Example 1:

Input:
N = 6
A[] = {1, 5, 1, 0, 6, 0}
X = 7
Output:
1

Explantion:
1, 5, 1, 0 are the four elements which makes sum 7.
 


Your Task:  
You don't need to read input or print anything. Your task is to complete the function find4Numbers() which takes the array A[], its size N and an integer X as inputs and returns true if combination is found else false. Driver code will print 1 or 0 accordingly.

 

Expected Time Complexity: O(N3)
Expected Auxiliary Space: O(1)

 

Constraints:
4 <= N <= 100
1 <= A[i] <= 1000
'''
#User function Template for python3
from collections import defaultdict
def find4Numbers(nums, n, X):
	# return true or false
	if n < 4:
		return []
	elif n == 4:
		if sum(nums) == X:
			return 1
		else:
			return 0
	nums.sort()

	dic = defaultdict(list)
	for index, num in enumerate(nums):
		dic[num].append(index)
	for i in range(n - 3):
		for j in range(i + 1, n - 2):
			for k in range(j + 1, n - 1):
				t = X - nums[i] - nums[j] - nums[k]
				if t in dic:
					count = 0
				if t == nums[i]:
					count = count + 1
				if t == nums[j]:
					count = count + 1
				if t == nums[k]:
					count = count + 1
				if len(dic[t]) > count:
					return 1
	return 0

print(find4Numbers([1, 5, 1, 0, 6, 0], 6, 7))