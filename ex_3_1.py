#!/usr/bin/env python

'makeTextFile.py -- create text file'

import os
ls = os.linesep
fname = "/media/rupinder/E28CD7918CD75E9B/Personal/Learning/Python/3.2"

# get filename
while True:

    if os.path.exists(fname):
        print("Error: '%s' already exists" % fname)
        exit()
    else:
        break
        

# get file content (text) lines
all = []
print("\nEnter lines ('.' by itself to quit).\n")

# loop unitl user terminates input
while True:
    entry = input('> ')
    if entry == '.':
        break
    else:
        all.append(entry)

# write lines to file with proper line-ending
fobj = open(fname, 'w')
fobj.writelines(['%s%s' % (x,ls) for x in all])
fobj.close()
print("Done")