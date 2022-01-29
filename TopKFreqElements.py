'''
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
'''
import collections
class Solution:
    def topKFrequent(self, nums, k):
        size = len(nums)
        dp = []
        for _ in range(size + 1):
        	dp.append([])
        num_freq = collections.Counter(nums)

        for key, count in num_freq.items():
        	dp[count].append(key)

        result = []
        print(num_freq)
        print(dp)
        for index in range(len(dp) - 1, 0, -1):
        	for n in dp[index]:
        		result.append(n)
        		if len(result) == k:
        			return result

obj = Solution()
print(obj.topKFrequent([4,1,-1,2,-1,2,3], 2))        