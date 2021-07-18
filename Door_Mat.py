'''
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be X. ( is an odd natural number, and  is  times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
Sample Designs

    Size: 7 x 21 
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
    
    Size: 11 x 33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
Input Format

A single line containing the space separated values of  and .

Constraints

Output Format

Output the design pattern.

Sample Input

9 27
Sample Output


0  ------------.|.------------
1  ---------.|..|..|.---------
2  ------.|..|..|..|..|.------
3  ---.|..|..|..|..|..|..|.---
4  ----------WELCOME----------
5  ---.|..|..|..|..|..|..|.---
6  ------.|..|..|..|..|.------
7  ---------.|..|..|.---------
8  ------------.|.------------
'''
data = raw_input().split()
N = int(data[0])
M = int(data[1])
mid = (N - 1)/2
lower = mid
upper = mid
flag = 0
str_put = ""
if(N % 2 != 0 and M == 3 * N):
	for i in range(N):
		
		for j in range(N):

			if i == mid:				
				bound = (N - 3)/2
				if j >= bound and j < (bound + 3):
					if flag == 0:
						flag = 1
						str_put = str_put + "-WELCOME-"
				else:
					str_put = str_put + "---"
			else:
				if j >= lower and j <= upper:
					str_put = str_put + ".|."
				else:
					str_put = str_put + "---"

		if i < mid:
			lower = lower - 1
			upper = upper + 1

		if i == mid:
			lower = lower + 1
			upper = upper - 1

		if i > mid:
			lower = lower + 1
			upper = upper - 1
		str_put = str_put + "\n"

print(str_put)