#!/usr/bin/env python
#Description:	take IDA PRO memory lines and print binary tree node.
from sys import argv

def find(st):
	#find a string in file
	for i in range(len_of_file):
		line = f.readline()
		if st in line:
			if st == line.split()[1]:
				return line
	return 0

def roll(num):
	#Roll the line
	for i in range(num):
		f.readline()

def retrun_right_left():
	#return right_node and left_node
	#roll(3) #rool junk mem
	right = f.readline() #read the addr of right node
	left = f.readline() # read the addr of left node
	right = right.split()
	left = left.split()
	return right[-1], left[-1]

def valid_data(st):
	if st[0] == "0":
		st = st[1:]
	return st

def build_data(l):
	sum = valid_data(l)
	l1 = f.readline()
	l1 = l1.split()
	if l1[-1] == "0":
		roll(2)
		return sum
	else:
		sum = valid_data(l1[-1]) + sum
		l2 = f.readline()
		l2 = l2.split()
		if l2[-1] == "0":
			roll(1)
			return sum
		else:
			sum = valid_data(l2[-1]) + sum
			l3 = f.readline()
			l3 = l3.split()
			if l3[-1] == "0":
				return sum
			else:
				sum = valid_data(l3[-1]) + sum
				return sum

def binTree(name, i):
	f.seek(0)
	line = find(name)

	line = line.split()
	line = build_data(line[-1])
	print "\t"*i + line

	right, left = retrun_right_left()
	
	if right == "0" or left == "0":
		return 0

	binTree(right, i+1)
	binTree(left, i+1)

def main(name, root):
	global f
	global len_of_file
	print "Parsing root node %s:" % root

	f = open(name, "r")
	len_of_file = len(list(f))

	binTree(root, 0)
	f.close()

if __name__ == '__main__':
	
	if len(argv) < 3:
		print "usage :\n%s <file.txt> <addr of root node>" % argv[0]
	else:
		main(argv[1], argv[2])
