'''
849. Maximize Distance to Closest Person
You are given an array representing a row of seats where seats[i] = 1 represents a person sitting in the ith seat, and seats[i] = 0 represents that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1
 

Constraints:

2 <= seats.length <= 2 * 104
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.
'''
class Solution:
	def maxDistToClosest(self, seats):
		forward = 0
		backward = 0
		size = len(seats)

		for seat in seats:
			if seat == 1:
				break
			forward += 1

		for seat in seats[::-1]:
			if seat == 1:
				break
			backward += 1

		count = 0
		max_dist = 0
		for index in range(forward, size - backward):
			if seats[index] == 1:
				count = 0
				continue
			count += 1
			max_dist = max(count, max_dist)

		print(forward, max_dist, backward)
		return max(forward, (max_dist + 1) // 2, backward)

obj = Solution()
print(obj.maxDistToClosest([1,0,0,0,1,0,1]))