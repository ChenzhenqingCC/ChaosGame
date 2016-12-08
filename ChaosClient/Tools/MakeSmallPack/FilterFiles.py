#coding=utf-8
import os
import stat
import os.path
import sys



fromdir_find = '../SmallPack/'
nopatch_find = '../Smp/'
thapatch_find = '../SmpTha/'

tagdir_find = '../../Client/Output/data/'

tagFloders = ["ccb", "map", "obj", "sound"];

def GetFiles(dir):
	newDir = dir
	if os.path.isfile(dir):
		fpath,fname =os.path.split(dir)
		rname, rext = os.path.splitext(fname)
		tagdir = dir.replace(tagdir_find,fromdir_find)
		if not os.path.exists(tagdir):
			os.chmod( dir, stat.S_IWRITE )
			os.remove(dir)
			#print("tagfile:" + tagdir + " not exists")
			#print(dir + " deleted")
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			GetFiles(newDir)

print(sys.argv[1])	
if sys.argv[1] == "nopatch":
	fromdir_find = nopatch_find
if sys.argv[1] == "thapatch":
	fromdir_find = thapatch_find
for floder in tagFloders:
	fromtagf = fromdir_find + floder
	totagf = tagdir_find + floder
	GetFiles(totagf)