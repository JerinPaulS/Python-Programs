'''
Orderly Queue
You are given a string s and an integer k. You can choose one of the first k letters of s and append it at the end of the string..

Return the lexicographically smallest string you could have after applying the mentioned step any number of moves.

 

Example 1:

Input: s = "cba", k = 1
Output: "acb"
Explanation: 
In the first move, we move the 1st character 'c' to the end, obtaining the string "bac".
In the second move, we move the 1st character 'b' to the end, obtaining the final result "acb".
Example 2:

Input: s = "baaca", k = 3
Output: "aaabc"
Explanation: 
In the first move, we move the 1st character 'b' to the end, obtaining the string "aacab".
In the second move, we move the 3rd character 'c' to the end, obtaining the final result "aaabc".
 

Constraints:

1 <= k <= s.length <= 1000
s consist of lowercase English letters.
'''
class Solution(object):
    def orderlyQueue(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        if k == 1:
        	size = len(s)
        	best_res = s
        	for index in range(size):
        		best_res = min(best_res, s[index:] + s[:index])
        	return best_res
        return "".join(sorted(s))


obj = Solution()
print(obj.orderlyQueue(s = "cba", k = 1))        