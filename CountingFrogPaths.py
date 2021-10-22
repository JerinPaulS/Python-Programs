'''
Counting Frog Paths
Problem
There is a frog initially placed at the origin of the coordinate plane. In exactly  second, the frog can either move up  unit, move right  unit, or stay still. In other words, from position , the frog can spend  second to move to:

After  seconds, a villager who sees the frog reports that the frog lies on or inside a square of side-length  with coordinates , , , . Calculate how many points with integer coordinates on or inside this square could be the frog's position after exactly  seconds

Input Format:

The first and only line of input contains four space-separated integers: , , , and .

Output Format:

Print the number of points with integer coordinates that could be the frog's position after  seconds.

Constraints:




Note that the Expected Output Feature for Custom Invocation is not supported for this contest. 

Sample Input
2 2 3 6
Sample Output
6
Time Limit: 2
Memory Limit: 256
Source Limit:
Explanation


The points shown are the points on or in the specified square, and those that are red are the points that the frog could be at after  seconds.
'''
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here
ip = input().split()
X, Y, s, T = int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])

que = []
visited = set()
visited.add((0, 0))

que.append((0, 0))
for _ in range(T):
	size = len(que)
	while size > 0:
		curr_x, curr_y = que.pop(0)
		if (curr_x + 1, curr_y) not in visited:
			que.append((curr_x + 1, curr_y))
			visited.add((curr_x + 1, curr_y))
		if (curr_x, curr_y + 1) not in visited:
			que.append((curr_x, curr_y + 1))		
			visited.add((curr_x, curr_y + 1))
		size = size - 1

result = 0

for pair in visited:
	if X <= pair[0] <= (X + s) and Y <= pair[1] <= (Y + s):
		result = result + 1

print(result)