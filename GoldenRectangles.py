'''
Golden rectangles
Problem
You have  rectangles. A rectangle is golden if the ratio of its sides is in between , both inclusive. Your task is to find the number of golden rectangles.

Input format

First line: Integer  denoting the number of rectangles
Each of the  following lines: Two integers  denoting the width and height of a rectangle
Output format

Print the answer in a single line.
Constraints



Sample Input
5
10 1
165 100
180 100
170 100
160 100

Sample Output
3
Time Limit: 1
Memory Limit: 256
Source Limit:
Explanation
There are three golden rectangles: (165, 100), (170, 100), (160, 100).
'''
count = int(input())
rects = []
result = 0
for _ in range(count):
    rect = list(map(int, input().split()))
    w, h = max(rect), min(rect)
    if 1.6 <= (w / h) <= 1.7:
    	result = result + 1

print(result)