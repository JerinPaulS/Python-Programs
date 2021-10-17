'''
Minimum operations to convert array A to B
Given two Arrays A[] and B[] of length N and M respectively. Find the minimum number of insertions and deletions on the array A[], required to make both the arrays identical.
Note: Array B[] is sorted and all its elements are distinct.

 

Example 1:

Input:
N = 5, M = 3
A[] = {1, 2, 5, 3, 1}
B[] = {1, 3, 5}
Output:
4
Explanation:
We need to delete 2 and replace it with 3.
This costs 2 steps. Further, we will have to
delete the last two elements from A to
obtain an identical array to B. Overall, it
results in 4 steps.
Example 2:
Input:
N = 2, M = 2
A[] = {1, 4}
B[] = {1, 4}
Output :
0
Explanation:
Both the Arrays are already identical.

Your Task:  
You don't need to read input or print anything. Your task is to complete the function minInsAndDel() which takes two integers N and M, and two arrays A of size N and B of size M respectively as input and returns the minimum insertions and deletions required.


Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(N)
'''
#User function Template for python3
import collections
import bisect
class Solution:
	def minInsAndDel(self, A, B, N, M):
		# code here 
		vec = []
		s = set(B)

		def LongestIncreasingSubsequenceLength(v):
			if len(v) == 0:
				return 0

			tail = [0 for i in range(len(v) + 1)]
			length = 1

			tail[0] = v[0]

			for i in range(1, len(v)):
				if v[i] > tail[length-1]:
					tail[length] = v[i]
					length += 1

				else:
					tail[bisect_left(tail, v[i], 0, length-1)] = v[i]

			return length

		for i in A:
			if i in s:
				vec.append(i)
		res = LongestIncreasingSubsequenceLength(vec)
		return abs(N - res) + abs(M - res)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.minInsAndDel(A,B,N,M))
# } Driver Code Ends