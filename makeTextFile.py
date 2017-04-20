#!/usr/bin/env Python

'makeTextFile.py -- create text file'

import os

ls = os.linesep

# get filename
while True:
    fname = input('Enter file name:')
    if os.path.exists(fname):
        print("ERROR: '%s' already exists" % fname)
    else:
        break

all = []
print("\nEnter lines ('.' by itself to quit).\n")

while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x, ls) for x in all])
fobj.close()

print('DONE!')
