'''
252. Meeting Rooms
Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

(0,8),(8,10) is not conflict at 8

Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation: 
(0,30), (5,10) and (0,30),(15,20) will conflict
Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation: 
Two times will not conflict 
'''

#Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
	"""
	@param intervals: an array of meeting time intervals
	@return: if a person could attend all meetings
	"""
	def canAttendMeetings(self, intervals):
		# Write your code here
		intervals.sort(key = lambda i : i.start)

		for meeting in range(1, len(intervals)):
			m1 = meeting[i - 1]
			m2 = meeting[i]

			if m1.end > m2.start:
				return False

		return True

obj = Solution()
print(obj.canAttendMeetings([(0,30),(5,10),(15,20)]))
print(obj.canAttendMeetings([(5,8),(9,15)]))