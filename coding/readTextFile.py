#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""read text file"""

file_name = raw_input(">")
print "Try open file '%s', if file '%s' exist." % (file_name, file_name)

try:
    file_obj = open(file_name, 'r')
except IOError, e:
    print "File '%s' not exist: " % file_name, e
else:
    for line in file_obj:
        print "%s\n" % line
    file_obj.close()

print "DONE"
