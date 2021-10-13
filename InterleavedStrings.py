'''
Interleaved Strings
Given strings A, B, and C, find whether C is formed by an interleaving of A and B.

An interleaving of two strings S and T is a configuration such that it creates a new string Y from the concatenation substrings of A and B and |Y| = |A + B| = |C|

For example:

A = "XYZ"

B = "ABC"

so we can make multiple interleaving string Y like, XYZABC, XAYBCZ, AXBYZC, XYAZBC and many more so here your task is to check whether you can create a string Y which can be equal to C.

Specifically, you just need to create substrings of string A and create substrings B and concatenate them and check whether it is equal to C or not.

Note: a + b is the concatenation of strings a and b.

Return true if C is formed by an interleaving of A and B, else return false.

Example 1:

Input:
A = YX, B = X, C = XXY
Output: 0
Explanation: XXY is not interleaving
of YX and X
Example 2:

Input:
A = XY, B = X, C = XXY
Output: 1
Explanation: XXY is interleaving of
XY and X.
Your Task:
Complete the function isInterleave() which takes three strings A, B and C as input and returns true if C is an interleaving of A and B else returns false. (1 is printed by the driver code if the returned value is true, otherwise 0.)

Expected Time Complexity: O(N * M)
Expected Auxiliary Space: O(N * M)
here, N = length of A, and M = length of B

Constraints:
1 ≤ length of A, B ≤ 100
1 ≤ length of C ≤ 200
'''
#Your task is to complete this Function \
import collections
class Solution:
    #function should return True/False
    def isInterleave(self, A, B, C):
        # Code here
        if len(C) != len(A) + len(B):
        	return False
        dp = collections.defaultdict(bool)
        
        def check(ptr, ptr1, ptr2):
        	if ptr == len(C):
        		return ptr1 == len(A) and ptr2 == len(B)

        	key = str(ptr1) + "*" + str(ptr2) + "*" + str(ptr)
        	if key in dp:
        		return dp[key]

        	if ptr1 == len(A):
        		if B[ptr2] == C[ptr]:
        			dp[key] = check(ptr + 1, ptr1, ptr2 + 1)
        		else:
        			dp[key] = False
        		return dp[key]
        	if ptr2 == len(B):
        		if A[ptr1] == C[ptr]:
        			dp[key] = check(ptr + 1, ptr1 + 1, ptr2)
        		else:
        			dp[key] = False
        		return dp[key]

        	res1 = False
        	res2 = False

        	if A[ptr1] == C[ptr]:
        		res1 = check(ptr + 1, ptr1 + 1, ptr2)
        	if B[ptr2] == C[ptr]:
        		res2 = check(ptr + 1, ptr1, ptr2 + 1)
        	dp[key] = res1 or res2
        	return dp[key]

        return check(0, 0, 0)

'''
#{ 
#  Driver Code Starts
#Initial template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr=input().strip().split()
        if Solution().isInterleave(arr[0], arr[1], arr[2]):
            print(1)
        else:
            print(0)
# contributed By: Harshit Sidhwa
# } Driver Code Ends
'''

obj = Solution()
print(obj.isInterleave("aabcc", "dbbca", "aadbcbbcac"))