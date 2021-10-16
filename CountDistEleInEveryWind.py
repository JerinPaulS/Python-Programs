'''
Count distinct elements in every window
Given an array of integers and a number K. Find the count of distinct elements in every window of size K in the array.

Example 1:

Input:
N = 7, K = 4
A[] = {1,2,1,3,4,2,3}
Output: 3 4 4 3
Explanation: Window 1 of size k = 4 is
1 2 1 3. Number of distinct elements in
this window are 3. 
Window 2 of size k = 4 is 2 1 3 4. Number
of distinct elements in this window are 4.
Window 3 of size k = 4 is 1 3 4 2. Number
of distinct elements in this window are 4.
Window 4 of size k = 4 is 3 4 2 3. Number
of distinct elements in this window are 3.
Example 2:

Input:
N = 3, K = 2
A[] = {4,1,1}
Output: 2 1
Your Task:
Your task is to complete the function countDistinct() which takes the array A[], the size of the array(N) and the window size(K) as inputs and returns an array containing the count of distinct elements in every contiguous window of size K in the array A[].

Expected Time Complexity: O(N).
Expected Auxiliary Space: O(N).

Constraints:
1 <= K <= N <= 105
1 <= A[i] <= 105 , for each valid i
'''
import collections
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        result = []
        freq_count = collections.Counter(A[:K])
        result.append(len(freq_count.keys()))
        print freq_count
        for index in range(K, N):
        	freq_count[A[index - K]] = freq_count[A[index - K]] - 1
        	if freq_count[A[index - K]] == 0:
        		freq_count.pop(A[index - K])
        	print freq_count
        	if freq_count.has_key(A[index]):
        		freq_count[A[index]] = freq_count[A[index]] + 1
        	else:
        		freq_count[A[index]] = 1
        	result.append(len(freq_count.keys()))
       	return result
'''
#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends
'''
obj = Solution()
print(obj.countDistinct([1,2,1,3,4,2,3],7,4))