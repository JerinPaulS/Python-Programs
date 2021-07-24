'''
163. Missing Ranges

Example 1:
Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Result: ['2', '4->49', '51->74', '76->99']

Example 2:
Input: nums= [], lower = 1, upper = 1
Result: ['1']

Example 3:
Input: nums = [], lower = -3, upper = -1
Result: ['-3->-1']

Example 4:
[-1], -1, -1
[]

Example 5:
[-1], -2, -1
['-2']


'''
class Solution(object):
	def findMissingRanges(self, nums, lower, upper):
		"""
		:type nums: list[int]
		:type lower: int
		:type upper: int
        :rtype: list[str]
		"""
		result = []

		if len(nums) == 0:
			result.append(self.format_ans(lower, upper))
			return result

		if lower < nums[0]:
			result.append(self.format_ans(lower, nums[0] - 1))

		for index in range(len(nums) - 1):
			if nums[index + 1] - nums[index] > 1:
				result.append(self.format_ans(nums[index] + 1, nums[index + 1] - 1))

		if nums[len(nums) - 1] < upper:
			result.append(self.format_ans(nums[len(nums) - 1] + 1, upper))
		
		return result

	def format_ans(self, a, b):
		if a == b:
			return str(a)
		else:
			return str(a) + "->" + str(b)

obj = Solution()
print(obj.findMissingRanges([0,1,3,50,75], 0, 99))
print(obj.findMissingRanges([], 1, 1))
print(obj.findMissingRanges([], -3, -1))
print(obj.findMissingRanges([-1], -1, -1))
print(obj.findMissingRanges([-1], -2, -1))