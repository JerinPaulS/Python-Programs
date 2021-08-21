'''
1588. Sum of All Odd Length Subarrays
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

A subarray is a contiguous subsequence of the array.

Return the sum of all odd-length subarrays of arr.

 

Example 1:

Input: arr = [1,4,2,5,3]
Output: 58
Explanation: The odd-length subarrays of arr and their sums are:
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
If we add all these together we get 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
Example 2:

Input: arr = [1,2]
Output: 3
Explanation: There are only 2 subarrays of odd length, [1] and [2]. Their sum is 3.
Example 3:

Input: arr = [10,11,12]
Output: 66
 

Constraints:

1 <= arr.length <= 100
1 <= arr[i] <= 1000

'''
class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        prefix_sum = [0, arr[0]]
        size = len(arr)
        for index in range(1, size):
        	prefix_sum.append(arr[index] + prefix_sum[-1])
        result = 0

        def calc(i, j):
        	print i, j
        	res = prefix_sum[j + 1] - prefix_sum[i]
        	return res

        for i in range(size):
        	result = result + arr[i]
        	j = i + 2
        	while j < size:
        		result = result + calc(i, j)
        		j = j + 2

        return result


obj = Solution()
print(obj.sumOddLengthSubarrays([1,4,2,5,3]))