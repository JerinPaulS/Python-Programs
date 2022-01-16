'''
763. Partition Labels
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.
Example 2:

Input: s = "eccbbbbdec"
Output: [10]
 

Constraints:

1 <= s.length <= 500
s consists of lowercase English letters.
'''
import collections
class Solution:
    def partitionLabels(self, s):
        result = []
        index_dict = collections.defaultdict(int)

        for index, char in enumerate(s):
        	index_dict[char] = index

        count = 0
        end = 0
        for index, char in enumerate(s):
        	count += 1
        	end = max(end, index_dict[char])
        	if index == end:
        		result.append(count)
        		count = 0
        return result

obj = Solution()
print(obj.partitionLabels("ababcbacadefegdehijhklij"))
#  a  b  a  b  c  b  a  c  a  d   e   f   e   g   d   e   h   i   j   h   k   l   i   j
#  0  1  2  3  4  5  6  7  8  9   10  11  12  13  14  15  16  17  18  19  20  21  22  23