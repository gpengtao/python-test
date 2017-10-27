#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""make text file"""

import os

sep = os.linesep

while True:
    file_name = raw_input()
    if os.path.exists(file_name):
        print "ERROR '%s' already exist" % file_name
    else:
        print "File '%s' not exist." % file_name
        break

all_line = []

print "\nEnter lines('.' by itself to quit)\n"

while True:
    line = raw_input(">")
    if line == '.':
        break
    else:
        all_line.append(line)

file_obj = open(file_name, 'w')
file_obj.writelines(['%s%s' % (line, sep) for line in all_line])
file_obj.close()

print "DONE"

