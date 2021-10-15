'''
All Unique Permutations of an array
Given an array arr[] of length n. Find all possible unique permutations of the array.


Example 1:

Input: 
n = 3
arr[] = {1, 2, 1}
Output: 
1 1 2
1 2 1
2 1 1
Explanation:
These are the only possible unique permutations
for the given array.
Example 2:

Input: 
n = 2
arr[] = {4, 5}
Output: 
4 5
5 4

Your Task:
You don't need to read input or print anything. You only need to complete the function uniquePerms() that takes an integer n, and an array arr of size n as input and returns a sorted list of lists containing all unique permutations of the array.


Expected Time Complexity:  O(n*n!)
Expected Auxilliary Space: O(n*n!)
 

Constraints:
1 ≤ n ≤ 10
1 ≤ arri ≤ 10
'''
#User function Template for python3

import collections
class Solution:
    def uniquePerms(self, arr, n):
        # code here
        result = []
        freq_count = collections.Counter(arr)

        def generate(current):
        	if len(current) == n:
        		result.append(current[:])
        		return
        	for num in freq_count:
        		if freq_count[num] > 0:
        			current.append(num)
        			freq_count[num] = freq_count[num] - 1
        			generate(current)
        			current.pop()
        			freq_count[num] = freq_count[num] + 1
        	return

        generate([])
        return result

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends