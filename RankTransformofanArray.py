'''
1331. Rank Transform of an Array
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 

Example 1:

Input: arr = [40,10,20,30]
Output: [4,1,2,3]
Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
Example 2:

Input: arr = [100,100,100]
Output: [1,1,1]
Explanation: Same elements share the same rank.
Example 3:

Input: arr = [37,12,28,9,100,56,80,5,12]
Output: [5,3,4,2,8,6,7,1,3]
 

Constraints:

0 <= arr.length <= 105
-109 <= arr[i] <= 109
'''
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dict_num = {}
        size = len(arr)
        for index in range(size):
        	dict_num[index] = arr[index]

        dict_num = sorted(dict_num.items(), key = lambda val: val[1])

        count = 1
        item = 1
        result = [0] * size
        for tup in dict_num:
        	if item != 1:
	        	if tup[1] == prev:
	        		count = count + 0
	        	else:
	        		count = count + 1
	        result[tup[0]] = count
        	prev = tup[1]
        	item = item + 1
        return result


obj = Solution()
print(obj.arrayRankTransform([37,12,28,9,100,56,80,5,12]))
print(obj.arrayRankTransform([1,1,1,1,1,1,2,1]))  