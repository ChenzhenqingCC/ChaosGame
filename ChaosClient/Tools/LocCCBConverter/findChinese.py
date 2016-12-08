#coding=utf-8
import os
import stat
import os.path
import re
import chardet
import codecs
from replaceChinese import *


fromdir_find = '../../../ChaosArt/res/ui_editor'

tagdir_find = './output.txt'

#re_words = re.compile(u"[\u4e00-\u9fa5]+")

def GetFiles(dir, clist, lan_list, spfiles):
	newDir = dir
	if os.path.isfile(dir):
		fpath,fname =os.path.split(dir)
		rname, rext = os.path.splitext(fname)
		if rext == '.ccb':
			f = open(dir, 'r')
			result = chardet.detect(f.read())
			f.close()
			if spfiles.has_key(fname):
				f = codecs.open(dir, 'r', spfiles[fname])
			else:
				f = open(dir, 'r')
			line = f.readline()
			print(dir)
			while line:
				if not spfiles.has_key(fname):
					resLine = chardet.detect(line)
					if result['encoding'].lower() == 'utf-8' or resLine['encoding'].lower() == 'utf-8':
						line = line.decode('utf-8')
					else:
						line = line.decode('gbk','ignore')
				res = re_words.findall(line)
				if len(res) > 0:
					line = line.strip()
					line = line.replace('<string>', '')
					line = line.replace('</string>', '')
					if not lan_list.has_key(line):
						clist[line] = dir
				line = f.readline()
			f.close()
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			GetFiles(newDir, clist, lan_list, spfiles)
	return clist

def findChinese():
	#1 从表中读取数据，以中文为key, 翻译为value
	lan_list = GetLanList({})
	spfiles = GetSpFiles({})
	#2 从ccb中挑中文，并过滤已有中文
	strlist = GetFiles(fromdir_find, {}, lan_list, spfiles)
	file_object = codecs.open(tagdir_find, "w", "utf-8")
	for k in strlist:
		file_object.write(k + u'\t')
		file_object.write(strlist[k])
		file_object.write(u"\r\n")
	file_object.close()

findChinese()
