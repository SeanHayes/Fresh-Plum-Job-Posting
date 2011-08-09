#!/usr/bin/python
"Solution to http://news.ycombinator.com/item?id=2833877"

import hashlib
import itertools
import string
import sys

s_list = ['d64a84456adc959f56de6af685d0dadd', '8d8a1b73876ca678cc3afa372e5199de']

def all_strings():
	str_length = 1
	while True:
		print 'Trying string length of %s' % str_length
		for s in itertools.product(string.printable, repeat=str_length):
			s = ''.join(s)
			yield s
		
		str_length += 1

found = 0

for s in all_strings():
	h = hashlib.md5()
	h.update(s)
	hashed_s = h.hexdigest()
	#print s
	if hashed_s in s_list:
		print '%s = %s' % (hashed_s, s)
		found += 1
	
	if found == 2:
		sys.exit(0)

