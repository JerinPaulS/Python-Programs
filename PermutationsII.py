'''
47. Permutations II
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10

'''
import collections
class Solution(object):
	def permuteUnique(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		result = []
		freq_count = collections.Counter(nums)

		def generate(current):
			if len(current) == len(nums):
				result.append(current[:])
				return
			for num in freq_count:
				if freq_count[num] > 0:
					current.append(num)
					freq_count[num] = freq_count[num] - 1
					generate(current)
					current.pop()
					freq_count[num] = freq_count[num] + 1
		generate([])
		return result


obj = Solution()
print(obj.permuteUnique([1,1,2]))        