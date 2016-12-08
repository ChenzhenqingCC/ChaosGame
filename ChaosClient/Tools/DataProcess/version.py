#-*- coding: utf-8 -*-
#!/usr/bin/python
from __future__ import division
import sys
import re
import fileinput

def replace(filename, key, value) :
    keyline = ""
    for line in fileinput.input(filename, inplace=1):
        if keyline != "":
            if None != re.search("string", line) :
                m1 = re.search(r'<string>(.*)</string>', line)
                old = m1.group(1)
                print line.replace(old, value),
                keyline = ""
        else :
            print line,
            if None != re.search(key, line) :
                keyline = line
    fileinput.close()    

def main():
    filename = sys.argv[1]
    key1 = "CFBundleVersion"
    key2 = "CFBundleShortVersionString"
    v1 = sys.argv[2]
    v2 = sys.argv[3]
    replace(filename, key1, v1)
    replace(filename, key2, v2)

if __name__ == '__main__':
    main()
 
