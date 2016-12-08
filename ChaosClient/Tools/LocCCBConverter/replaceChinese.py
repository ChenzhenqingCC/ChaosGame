#coding=utf-8
import sys
import os
import stat
import os.path
import re
import xlrd
import chardet
import codecs


language = sys.argv[1]

relate_path = sys.argv[2]

fromdir = relate_path + '/ChaosArt/res/loc/' + language + '/ccb_text/text.xlsx'

tagdir = relate_path + '/ChaosArt/res/ui_editor'

to_end_path = '/ChaosArt/res/loc/' + language + '/ui_editor'

todir = relate_path +  to_end_path

data = xlrd.open_workbook(fromdir)

table = data.sheet_by_name(u'main')

nrows = table.nrows

spftable = data.sheet_by_name(u'spfiles')

sprows = spftable.nrows


spfiles = {}

re_words = re.compile(u"[\u4e00-\u9fa5]+")



def mkdir(path):
 
	# 去除首位空格
	path=path.strip()
	# 去除尾部 \ 符号
	path=path.rstrip("\\")
 
	# 判断路径是否存在
	# 存在     True
	# 不存在   False
	isExists=os.path.exists(path)
 
	# 判断结果
	if not isExists:
		# 如果不存在则创建目录
		print path+' created'
		# 创建目录操作函数
		os.makedirs(path)
		return True
	else:
		# 如果目录存在则不创建，并提示目录已存在
		print path+' existed'
		return False

def convert( filename, in_enc = "GBK", out_enc="UTF-8" ):
		print "convert " + filename
		print(in_enc)
		os.chmod( filename, stat.S_IWRITE )
		content = open(filename).read()  
		new_content = content.decode(in_enc).encode(out_enc)  
		f = open(filename, 'w')
		f.write(new_content)
		f.close()  
		print " done"  

def convertFloder(dir):
	newDir = dir
	if os.path.isfile(dir):
		fpath,fname =os.path.split(dir)
		rname, rext = os.path.splitext(fname)
		if rext == '.ccb':
			f = open(dir, 'r')
			result = chardet.detect(f.read())
			f.close()
			if result['encoding'] == 'utf-8':
				a = 0
			else:
				convert(dir, result['encoding'])
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			convertFloder(newDir)

def CheckFiles(dir, clist, spfiles):
	newDir = dir
	if os.path.isfile(dir):
		fpath,fname =os.path.split(dir)
		rname, rext = os.path.splitext(fname)
		if rext == '.ccb':
			f = open(dir, 'r')
			result = chardet.detect(f.read())
			f.close()
			
			if spfiles.has_key(fname):
				ff = codecs.open(dir, 'r', spfiles[fname])
			else:
				ff = open(dir, 'r')
				
			lines=ff.readlines()
			ff.close()
			flen=len(lines)-1
			bch = False
			print(dir)
			print(result['encoding'])
			for i in range(flen):
				line = lines[i]
				if not spfiles.has_key(fname):
					resLine = chardet.detect(line)
					if result['encoding'].lower() == 'utf-8' or resLine['encoding'].lower() == 'utf-8':
						line = line.decode('utf-8')
					else:
						line = line.decode('gbk','ignore')
				res = re_words.findall(line)
				if len(res) > 0:
					tline = line.strip()
					tline = tline.replace('<string>', '')
					tline = tline.replace('</string>', '')
					if clist.has_key(tline):
						#print(tline)
						line = line.replace(tline,clist[tline])
						bch = True
				lines[i] = line.encode('utf-8')
			if bch:
					outdir = dir.replace(tagdir, todir)
					pp,fname = os.path.split(outdir);
					print("output:" + outdir)
					mkdir(pp)
					open(outdir,'w').writelines(lines)
	elif os.path.isdir(dir):  
		for s in os.listdir(dir):
			newDir=os.path.join(dir,s)
			CheckFiles(newDir, clist, spfiles)
			
def GetLanList(lan_list):
	#lan_list = {}
	for i in range(2, nrows):
			rowval = table.row_values(i)
			if isinstance(rowval[2], float):
					tagstr = '%d' %rowval[2]
					lan_list[rowval[0]] = tagstr.decode('utf-8')
			else:
					lan_list[rowval[0]] = rowval[2]
	return lan_list

def GetSpFiles(sp_list):
	for i in range(0, sprows):
			rowval = spftable.row_values(i)
			if isinstance(rowval[1], float):
					tagstr = '%d' %rowval[1]
					sp_list[rowval[0]] = tagstr.decode('utf-8')
			else:
					sp_list[rowval[0]] = rowval[1]
	return sp_list 
	
def replaceChinese():
		#1 从表中读取数据，以中文为key, 翻译为value
		lan_list = GetLanList({})
		spfiles = GetSpFiles({})
		#2 替换中文
		CheckFiles(tagdir, lan_list, spfiles)