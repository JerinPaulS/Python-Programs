'''
Array of Doubled Pairs
Given an array of integers arr of even length, return true if and only if it is possible to reorder it such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2.

 

Example 1:

Input: arr = [3,1,3,6]
Output: false
Example 2:

Input: arr = [2,1,2,6]
Output: false
Example 3:

Input: arr = [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: arr = [1,2,4,16,8,4]
Output: false
 

Constraints:

0 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105
'''
import collections
class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        freq = defaultdict(int)
        for x in arr:
        	freq[x] = freq[x] + 1
        
        for x in sorted(freq, key = abs): 
            if freq[2 * x] < freq[x]:
            	return False 
            freq[2 * x] = freq[2 * x] - freq[x]
        return True

obj = Solution()
print(obj.canReorderDoubled([1,2,4,8]))
print(obj.canReorderDoubled([3,1,3,6]))
print(obj.canReorderDoubled([2,1,2,6]))
print(obj.canReorderDoubled([4,-2,2,-4]))
print(obj.canReorderDoubled([1,2,4,16,8,4]))

'''
		index_hash = {}
        size = len(arr)
        result = []
        for index in range(size):
        	if index_hash.has_key(arr[index]):
        		index_hash[arr[index]].append(index)
        	else:
        		temp = [index]
        		index_hash[arr[index]] = temp

        for num in arr:
        	if num == 0 and len(index_hash[num]) > 0:
        		if index_hash[num] % 2 == 0:
        			result.append(num)
        			result.append(num)
        			index_hash[num].pop(0)
        			index_hash[num].pop(0)

        	elif index_hash.has_key(num * 2) and len(index_hash[num * 2]) != 0 and len(index_hash[num]) != 0:
        		result.append(num)
        		result.append(arr[index_hash[num * 2][0]])
        		if len(index_hash[num * 2]) != 0:
        			index_hash[num * 2].pop(0)
        		if len(index_hash[num]) != 0:
        			index_hash[num].pop(0)

        print result

        if len(result) != size:
        	return False
        else:
        	return True
'''