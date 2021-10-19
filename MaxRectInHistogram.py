'''
Maximum Rectangular Area in a Histogram
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit, there will be N bars height of each bar will be given by the array arr.

Example 1:

Input:
N = 7
arr[] = {6,2,5,4,5,1,6}
Output: 12
Explanation: 


Example 2:

Input:
N = 8
arr[] = {7 2 8 9 1 3 6 5}
Output: 16
Explanation: Maximum size of the histogram 
will be 8  and there will be 2 consecutive 
histogram. And hence the area of the 
histogram will be 8x2 = 16.
Your Task:
The task is to complete the function getMaxArea() which takes the array arr[] and its size N as inputs and finds the largest rectangular area possible and returns the answer.

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 ≤ N ≤ 106
1 ≤ arr[i] ≤ 1012
'''
#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
    def getMaxArea(self,histogram):
        #code here
        n = len(histogram)
        lstack = []
        ltop = -1
        rstack = []
        left = [0] * n
        right = [0] * n
        rtop = -1 
        for i in range(n):
            while len(lstack) != 0 and histogram[lstack[ltop]] >= histogram[i]:
                lstack.pop(ltop)
                ltop -= 1
            if len(lstack) == 0:
                left[i] = 0
                lstack.append(i)
                ltop += 1
            else:
                left[i] = lstack[ltop] + 1
                lstack.append(i)
                ltop += 1
        #filling right array
        for j in range(n-1, -1, -1):
            while len(rstack) != 0 and histogram[rstack[rtop]] >= histogram[j]:
                rstack.pop(rtop)
                rtop -= 1
            if len(rstack) == 0:
                right[j] = n - 1
                rstack.append(j)
                rtop += 1
            else:
                right[j] = rstack[rtop] - 1
                rstack.append(j)
                rtop += 1
        ans = -float('inf')
        for i in range(n):
            area = histogram[i] * (right[i] - left[i] + 1)
            ans = max(ans, area)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends

'''

		N, max_height = len(histogram), 0
        stack = []
        for i, height in enumerate(histogram + [-float('inf')]):
            start = i
            while stack and stack[-1][1] >= height:
                index, value = stack.pop()
                max_height = max(max_height, value * (i-index))
                start = index
            stack.append((start, height))
        
        return max_height
'''      