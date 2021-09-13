'''
40. Combination Sum II
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''
import collections
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()

        def generate(pos, total, curr):
        	if total == 0:
        		result.append(curr[:])
        	if total <= 0:
        		return
    		prev = -1
        	for index in range(pos, len(candidates)):
        		if prev == candidates[index]:
        			continue
        		curr.append(candidates[index])
        		generate(index + 1, total - candidates[index], curr)
        		curr.pop()
        		prev = candidates[index]

        generate(0, target, [])
        return result

obj = Solution()
print(obj.combinationSum2([10,1,2,7,6,1,5], 8))        