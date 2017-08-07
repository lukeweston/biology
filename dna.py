#!/usr/bin/python
import time

# Print DNA strand animation
# Thanks James :)

DNA = """ O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O
O---o
 O-o
  O
 o-O
o---O"""

lists = DNA.split('\n')
		
while 1:
	for line in lists:
		print line
		time.sleep(0.1)
