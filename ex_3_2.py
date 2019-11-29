#!

'readTextFile.py -- read and display text file'

#get filename
fname = input("Enter filename: ")


#attempt to open file for reading
try:
    fobj = open(fname,'r')
except IOError as e:
    print("*** file open error:",e)
else:
    #display cpmtemts to the screen
    for eachLine in fobj:
        print(eachLine),
    fobj.close()
