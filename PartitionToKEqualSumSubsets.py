'''
Partition to K Equal Sum Subsets
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
 

Constraints:

1 <= k <= nums.length <= 16
1 <= nums[i] <= 104
The frequency of each element is in the range [1, 4].
'''
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        target, remainder = divmod(sum(nums), k)

        if remainder > 0:
            return False

        def backtrack(curr_sum, index , k):
            if k == 0:
                return True

            if curr_sum == target:
                return backtrack(0, 0, k - 1)

            for i in range(index, len(nums)):
                num = nums[i]
                if curr_sum + num <= target and not visited[i]:
                    visited[i] = True
                    if backtrack(curr_sum + num, i + 1, k):
                        return True
                    visited[i] = False

            return False

        size = len(nums)
        visited = [False] * size
        return backtrack(0, 0, k)