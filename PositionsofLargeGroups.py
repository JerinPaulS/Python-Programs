'''
830. Positions of Large Groups
In a string s of lowercase letters, these letters form consecutive groups of the same character.

For example, a string like s = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z", and "yy".

A group is identified by an interval [start, end], where start and end denote the start and end indices (inclusive) of the group. In the above example, "xxxx" has the interval [3,6].

A group is considered large if it has 3 or more characters.

Return the intervals of every large group sorted in increasing order by start index.

 

Example 1:

Input: s = "abbxxxxzzy"
Output: [[3,6]]
Explanation: "xxxx" is the only large group with start index 3 and end index 6.
Example 2:

Input: s = "abc"
Output: []
Explanation: We have groups "a", "b", and "c", none of which are large groups.
Example 3:

Input: s = "abcdddeeeeaabbbcd"
Output: [[3,5],[6,9],[12,14]]
Explanation: The large groups are "ddd", "eeee", and "bbb".
Example 4:

Input: s = "aba"
Output: []
 

Constraints:

1 <= s.length <= 1000
s contains lower-case English letters only.
'''
class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        result = []
        start = 0
        for index in range(len(s) - 1):
        	if s[index] != s[index + 1]:
        		temp = [start, index]
        		if index - start + 1 >= 3:
        			result.append(temp)
        		start = index + 1
        if len(s) - start >= 3:
        	result.append([start, len(s) - 1])
        return result

obj = Solution()
print(obj.largeGroupPositions("babaaaabbb"))
print(obj.largeGroupPositions("abcdddeeeeaabbbcd"))