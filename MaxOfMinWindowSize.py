'''
Maximum of minimum for every window size
Given an integer array. The task is to find the maximum of the minimum of every window size in the array.
Note: Window size varies from 1 to the size of the Array.

Example 1:

Input:
N = 7
arr[] = {10,20,30,50,10,70,30}
Output: 70 30 20 10 10 10 10 
Explanation: 
1.First element in output
indicates maximum of minimums of all
windows of size 1.
2.Minimums of windows of size 1 are {10},
 {20}, {30}, {50},{10}, {70} and {30}. 
 Maximum of these minimums is 70. 
3. Second element in output indicates
maximum of minimums of all windows of
size 2. 
4. Minimums of windows of size 2
are {10}, {20}, {30}, {10}, {10}, and
{30}.
5. Maximum of these minimums is 30 
Third element in output indicates
maximum of minimums of all windows of
size 3. 
6. Minimums of windows of size 3
are {10}, {20}, {10}, {10} and {10}.
7.Maximum of these minimums is 20. 
Similarly other elements of output are
computed.
Example 2:

Input:
N = 3
arr[] = {10,20,30}
Output: 30 20 10
Explanation: First element in output
indicates maximum of minimums of all
windows of size 1.Minimums of windows
of size 1 are {10} , {20} , {30}.
Maximum of these minimums are 30 and
similarly other outputs can be computed
Your Task:
The task is to complete the function maxOfMin() which takes the array arr[] and its size N as inputs and finds the maximum of minimum of every window size and returns an array containing the result. 

Expected Time Complxity : O(N)
Expected Auxilliary Space : O(N)

Constraints:
1 <= N <= 105
1 <= arr[i] <= 106
'''
class Solution:
    
    #Function to find maximum of minimums of every window size.
    def maxOfMin(self,arr,n):
    # code here
        stack = []
        result = [0] * n
        dp = [0] * (n + 1)
        for i in range(n):
            while len(stack) > 0 and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if len(stack) == 0:
                dp[i] = i + 1
            else:
                dp[i] = i - stack[-1]
            stack.append(i)
        
        while len(stack) > 0:
            stack.pop()
            
        for i in range(n - 1, -1, -1):
            while len(stack) > 0 and arr[stack[-1]] > arr[i]:
                stack.pop()
            if len(stack) == 0:
                dp[i] = dp[i] + n - 1 - i
            else:
                dp[i] = dp[i] + stack[-1] - i - 1
            stack.append(i)
            result[dp[i] - 1] = max(result[dp[i] - 1], arr[i])
            
        for i in range(n - 2, -1, -1):
            result[i] = max(result[i + 1], result[i])
        return result