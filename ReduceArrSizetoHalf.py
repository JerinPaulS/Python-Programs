'''
Given an array arr.  You can choose a set of integers and remove all the occurrences of these integers in the array.

Return the minimum size of the set so that at least half of the integers of the array are removed.

 

Example 1:

Input: arr = [3,3,3,3,5,5,5,2,2,7]
Output: 2
Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
Possible sets of size 2 are {3,5},{3,2},{5,2}.
Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has size greater than half of the size of the old array.
Example 2:

Input: arr = [7,7,7,7,7,7]
Output: 1
Explanation: The only possible set you can choose is {7}. This will make the new array empty.
Example 3:

Input: arr = [1,9]
Output: 1
Example 4:

Input: arr = [1000,1000,3,7]
Output: 1
Example 5:

Input: arr = [1,2,3,4,5,6,7,8,9,10]
Output: 5
 

Constraints:

1 <= arr.length <= 10^5
arr.length is even.
1 <= arr[i] <= 10^5
'''
import collections
class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        removed = 0
        mid = len(arr) / 2
        num_freq = collections.Counter(arr)
        count = 0
        for val in sorted(num_freq.values(), reverse = True):        	
        	removed = removed + val
        	count = count + 1        	
        	if removed >= mid:
        		return count
        return 0


obj = Solution()
print(obj.minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(obj.minSetSize([7,7,7,7,7,7]))
print(obj.minSetSize([1,9]))
print(obj.minSetSize([1000,1000,3,7]))
print(obj.minSetSize([1,2,3,4,5,6,7,8,9,10]))

'''
if len(arr) < 2 or len(arr) % 2 != 0:
        	return 0
        num_arr = []
        num_freq = []
        curr_len = len(arr)
        mid = len(arr) / 2
        count = 0
        for num in arr:
        	if num not in num_arr:
        		num_arr.append(num)
        		num_freq.append(arr.count(num))
        while curr_len > mid:
        	curr_len = curr_len - max(num_freq)
        	num_arr.remove(num_arr[num_freq.index(max(num_freq))])
        	num_freq.remove(max(num_freq))
        	count = count + 1
        return count
'''