#!/usr/bin/env python

'readTextFile.py -- read and display text file'

fname = input('Enter file name:')
print()

try:
    fobj = open(fname, 'r')
except IOError as e:
    print("*** file open error:", e)
else:
    for eachLine in fobj:
        print(eachLine),
    fobj.close()
