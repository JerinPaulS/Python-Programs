'''
You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:

#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
The center of the rangoli has the first alphabet letter a, and the boundary has the  alphabet letter (in alphabetical order).

Function Description

Complete the rangoli function in the editor below.

rangoli has the following parameters:

int size: the size of the rangoli
Returns

string: a single string made up of each of the lines of the rangoli separated by a newline character (\n)
Input Format

Only one line of input containing , the size of the rangoli.

Constraints


Sample Input

5
Sample Output

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
'''
def print_rangoli(size):
	str_out = ""
	if size == 1:
		str_out = "a"
	else:
		for i in range(1, (2 * size)):
			n = 0
			n1 = 0
			m = 0
			m1 = 0
			for j in range(1, (2 * size)):
				
				if i <= size:
					if j <= size:
						if j > size - i:						
							str_out = str_out + str(chr(96 + size - n)) + "-"
							n = n + 1
						else:
							str_out = str_out + "--"
					else:					
						if j != (2 * size) - 1:
							if j < size + i:						
								str_out = str_out + str(chr(97 + size - i + n1 + 1)) + "-"
								n1 = n1 + 1
							else:
								str_out = str_out + "--"
						else:
							if j < size + i:						
								str_out = str_out + str(chr(97 + size - i + n1 + 1))
								n1 = n1 + 1
							else:
								str_out = str_out + "-"

				else:
					if j <= size:
						if j > i - size:						
							str_out = str_out + str(chr(96 + size - m)) + "-"
							m = m + 1
						else:
							str_out = str_out + "--"
					else:
						if j != (2 * size) - 1:
							if j < (2 *size) - (i - size):						
								str_out = str_out + str(chr(97 - size + i + m1 + 1)) + "-"
								m1 = m1 + 1
							else:
								str_out = str_out + "--"
						else:
							if j < (2 *size) - (i - size):						
								str_out = str_out + str(chr(97 - size + i + m1 + 1))
								m1 = m1 + 1
							else:
								str_out = str_out + "-"
				
			str_out = str_out + "\n"
	print(str_out)


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)