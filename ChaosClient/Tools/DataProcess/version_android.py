#-*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import division
import sys
import re
import fileinput
import os
import stat

def replaceInFile(filename, strFrom, strTo):  
    for line in fileinput.input(filename, inplace=True):  
        if re.search(strFrom, line):  
            line = line.replace(strFrom, strTo)  
        print line,    

def main():
    filename = sys.argv[1]
    os.chmod( filename, stat.S_IWRITE )
    key1 = "android:versionCode=\"1\""
    key2 = "android:versionName=\"1.0\""
    v1 = sys.argv[2]
    v2 = sys.argv[3]
    newkey1 = "android:versionCode="
    newkey1 += "\""
    newkey1 += v1
    newkey1 += "\""
    newkey2 = "android:versionName="
    newkey2 += "\""
    newkey2 += v2
    newkey2 += "\""
    replaceInFile(filename, key1, newkey1)
    replaceInFile(filename, key2, newkey2)

if __name__ == '__main__':
    main()
 
