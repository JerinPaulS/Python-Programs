'''
997. Find the Town Judge
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
Example 4:

Input: n = 3, trust = [[1,2],[2,3]]
Output: -1
Example 5:

Input: n = 4, trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
Output: 3
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
'''
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        if len(trust) == 0 and n == 1:
        	return n
        elif len(trust) == 0 and n > 1:
        	return -1
        common_person = {}
        judge_person = {}

        for t in trust:
        	p1 = t[0]
        	p2 = t[1]

        	if common_person.has_key(p1):
        		common_person[p1] = common_person[p1] + 1
        	else:
        		common_person[p1] = 1

        	if judge_person.has_key(p2):
        		judge_person[p2] = judge_person[p2] + 1
        	else:
        		judge_person[p2] = 1

        for index in range(1, n + 1):
        	if common_person.has_key(index) == False and judge_person.has_key(index) == True and judge_person[index] == n - 1:
        		return index

        return -1